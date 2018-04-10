""" Provides modification functions for RecipeUrl objects """

from operations import crud
from models.core.recipe import Recipe
from models.core.recipe_step import RecipeStep
from models.core.quantity import Quantity
from operations.recipe import recipe_url_modify, recipe_url_lookup, recipe_lookup, \
                                recipe_step_modify, quantity_modify

from operations.helper import quantity_helper
import urllib

# TODO: Only add recipe this info if user "edits"
def add_recipe_info(user_id, details={}):
    """ Add a Recipe (and all its ingredients and steps)"""
    if len(details) == 0:
        raise Exception("No details given to add recipe")


    # Add URL to Recipe URL Table
    recipe_url = recipe_url_lookup.by_url(details['url'])
    if not recipe_url:
        recipe_url_modify.add(details['url'])
        recipe_url = recipe_url_lookup.by_url(details['url'])


    recipe = recipe_lookup.by_user_url_id(user_id, recipe_url.id)
    if recipe:
        return False, None # Already have this recipe, return False

    # Add Recipe information to Database and get it's ID
    recipe_obj = Recipe(name=details['name'],
                        description=details['description'],
                        user_id=user_id,
                        url_id=recipe_url.id)
    add(recipe_obj)
    recipe = recipe_lookup.by_user_url_id(user_id, recipe_url.id)


    # Add steps to database
    step_num = 1
    for step in details['steps']:
        if len(step.strip()) == 0: continue
        recipe_step = RecipeStep(recipe_id=recipe.id, description=step, num=step_num)
        recipe_step_modify.add(recipe_step)
        step_num += 1


    # Add all ingredients to database
    for ingrdt in details['ingredients']:
        ingredient, measurement, amount = quantity_helper.parse(ingrdt)

        # Add to quantity table
        if measurement:
            quantity_modify.add(Quantity(ingredient_id=ingredient, \
                                         measurement_id=measurement, \
                                         recipe_id=recipe.id, \
                                         amount=amount))
        else:
            quantity_modify.add(Quantity(ingredient_id=ingredient, \
                                         recipe_id=recipe.id, \
                                         amount=amount))
    # Save the image of the recipe
    img_url = details['image_url']
    #print img_url
    file_name = "app/static/img/" + str(recipe_url.id) + ".jpg"
    #print file_name
    try:
        urllib.urlretrieve(img_url, file_name)
    except Exception as e:
        print(e)
    print "test"

    return True, recipe.id



def add(recipe_obj):
    """ Add a recipe object """
    crud.add(recipe_obj)

def save(recipe_obj, form):
    """ Save a recipe object from a form """
    session = crud.pre_save()
    values = form.to_dict()
    del values['csrf_token']
    del values['submit']
    session.query(Recipe).filter(Recipe.id == recipe_obj.id).update(values)
    crud.save_update(session)


def delete(recipe_obj):
    """ Delete a recipe object """

    if recipe_obj.steps:
        for step in recipe_obj.steps:
            recipe_step_modify.delete(step)

    for quant_obj in recipe_obj.quantity:
        quantity_modify.delete(quant_obj)

    crud.delete(recipe_obj)
