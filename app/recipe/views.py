""" Views associated with recipe """

from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required
from flask.ext.login import current_user

from app.recipe import recipe
from app.recipe.forms import URLForm, EditRecipeForm, EditRecipeStepForm, EditIngredientForm
from operations.helper import url_parse

from operations.recipe import recipe_lookup, recipe_modify, recipe_step_lookup, \
                               recipe_step_modify, quantity_lookup, quantity_modify

@recipe.route('/recipe/add', methods=['GET', 'POST'])
@login_required
def add():
    """ Add a Recipe """
    form = URLForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            #If this is not a valid recipe, return a defualt message
            try:
              sucessful, recipe_id = url_parse.allrecipes(request.form['URL'], request.form['category_id'], current_user.id)

              #if not sucessful, tell user they already have the object
              if not sucessful:
                  flash('Already have that recipe')
                  return render_template('recipe/add_recipe.html', form=form)
              return redirect(url_for('recipe.view', recipe_id=recipe_id))

            except:
              flash('ERROR: This is not a valid recipe!')
              return render_template('recipe/add_recipe.html', form=form)


    return render_template('recipe/add_recipe.html', form=form)

@recipe.route('/recipe/view/', methods=['GET'])
@login_required
def view():
    """ View a specific Recipe """
    recipe_obj = recipe_lookup.by_id(request.args.get('recipe_id'))
    return render_template('recipe/view.html', recipe=recipe_obj)


# TODO: Add decorator to ensure user own's this recipe
@recipe.route('/recipe/edit_recipe/', methods=['GET', 'POST'])
@login_required
def edit_recipe():
    """ Edit a Recipe Name """
    form = EditRecipeForm(request.form)
    recipe_obj = recipe_lookup.by_id(request.args.get('recipe_id'))

    if request.method == "POST":
        if form.validate_on_submit():
            recipe_modify.save(recipe_obj, request.form)
            return redirect(url_for('recipe.view', recipe_id=recipe_obj.id))
    else:
        form = EditRecipeForm(obj=recipe_obj)

    return render_template('recipe/edit_recipe.html', \
                            var={'form':form,
                                 'recipe_id':recipe_obj.id
                                }
                          )



# TODO: Add decorator to ensure user own's this recipe
@recipe.route('/recipe/edit_step/', methods=['GET', 'POST'])
@login_required
def edit_step():
    """ Edit a Recipe Step """
    form = EditRecipeStepForm(request.form)
    recipe_step = recipe_step_lookup.by_id(request.args.get('recipe_step_id'))

    if request.method == "POST":
        if form.validate_on_submit():
            recipe_step_modify.save(recipe_step, request.form)
            return redirect(url_for('recipe.view', recipe_id=recipe_step.recipe_id))
    else:
        form = EditRecipeStepForm(obj=recipe_step)

    return render_template('recipe/edit_recipe_step.html', \
                            var={'form':form, 'recipe_step_id':recipe_step.id})


# TODO: Add decorator to ensure user own's this recipe
@recipe.route('/recipe/edit_ingrd/', methods=['GET', 'POST'])
@login_required
def edit_ingredient():
    """ Edit an Ingredient """
    form = EditIngredientForm(request.form)
    ingredient = quantity_lookup.by_id(request.args.get('quantity_id'))
    if request.method == "POST":
        if form.validate_on_submit():
            quantity_modify.save(ingredient, request.form)
            return redirect(url_for('recipe.view', recipe_id=ingredient.recipe_id))
    else:
        form = EditIngredientForm(description=ingredient.description())

    return render_template('recipe/edit_ingredient.html', \
                            var={'form':form, 'quantity_id':ingredient.id})




@recipe.route('/recipe/view_all')
@login_required
def view_all():
    """ View all Recipes """
    all_recipes = recipe_lookup.get_all(current_user.id)

    return render_template('recipe/view_all.html', all_recipes=all_recipes)



@recipe.route('/recipe/delete_recipe', methods=['POST'])
@login_required
def delete_recipe():
    """ Delete a specific recipe """
    if request.method == 'POST':
        recipe_id = request.form['recipe_id']
        recipe = recipe_lookup.by_user_recipe_id(current_user.id, recipe_id)
        if recipe:
            recipe_modify.delete(recipe)
            flash("Successfully deleted recipe")

    return redirect(url_for('recipe.view_all'))


@recipe.route('/recipe/delete_ingredient', methods=['POST'])
@login_required
def delete_ingredient():
    """ Delete a specific ingredient """
    if request.method == 'POST':
        quantity_id = request.form['quantity_id']
        recipe_id = request.form['recipe_id']
        quantity = quantity_lookup.by_id(quantity_id)
        if quantity:
            quantity_modify.delete(quantity)
            flash("Successfully deleted ingredient")

        return redirect(url_for('recipe.view', recipe_id=recipe_id))

    return redirect(url_for('recipe.view_all'))




@recipe.route('/recipe/category/', methods=['GET'])
@login_required
def view_category():
    """ View a  Recipe """
    category = request.args.get('category_id')
    all_recipes = recipe_lookup.by_category(category)

    return render_template('recipe/view_all.html', all_recipes=all_recipes)
