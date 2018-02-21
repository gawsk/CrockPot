""" Provides modification functions for RecipeUrl objects """

from operations import crud
from models.core.recipe import Recipe
from models.core.recipe_step import RecipeStep
from models.core.ingredient import Ingredient
from models.core.measurement import Measurement
from models.core.quantity import Quantity
from operations.recipe import recipe_url_modify, recipe_url_lookup, recipe_lookup, \
                                recipe_step_modify, ingredient_lookup, ingredient_modify, \
                                measurement_modify, measurement_lookup, quantity_modify

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


    recipe = recipe_lookup.by_user_url(user_id, recipe_url.id)
    if recipe:
        return False # Already have this recipe, return False

    # Add Recipe information to Database and get it's ID
    recipe_obj = Recipe(name=details['name'],
                        description=details['description'],
                        user_id=user_id,
                        url_id=recipe_url.id)
    add(recipe_obj)
    recipe = recipe_lookup.by_user_url(user_id, recipe_url.id)


    # Add steps to database
    step_num = 1
    for step in details['steps']:
        if len(step.strip()) == 0: continue
        recipe_step = RecipeStep(recipe_id=recipe.id, description=step, num=step_num)
        recipe_step_modify.add(recipe_step)
        step_num += 1

    measurements = {'teaspoons', 'tablespoons', 'cup', 'cups', 'pints', 'pint', 'quarts', 'quart', \
                        'ounce', 'ounces', 'dash', 'pinch', 'cube', 'cubes'}

    # Add all ingredients to database
    for ingrdt in details['ingredients']:
        ingrdt = ingrdt.split(' ')
        quantity = ingrdt[0].encode('utf8')
        measurement, increments = None, None
        if ingrdt[1] in measurements:
            increments = ingrdt[1]
            description = ' '.join(ingrdt[2:])
            measurement = measurement_lookup.by_name(increments)
        else:
            description = ' '.join(ingrdt[1:])

        ingredient = ingredient_lookup.by_name(description)
        if ingredient is None:
            ingredient_modify.add(Ingredient(name=description))
            ingredient = ingredient_lookup.by_name(description)

        if measurement is None and increments != None:
            measurement_modify.add(Measurement(name=increments))
            measurement = measurement_lookup.by_name(increments)

        # Add to quantity table
        if measurement:
            quantity_modify.add(Quantity(ingredient_id=ingredient.id, \
                                         measurement_id=measurement.id, \
                                         recipe_id=recipe.id, \
                                         amount=quantity))
        else:
            quantity_modify.add(Quantity(ingredient_id=ingredient.id, \
                                         recipe_id=recipe.id, \
                                         amount=quantity))
    return True



def add(recipe_obj):
    """ Add a recipe object """
    crud.add(recipe_obj)
