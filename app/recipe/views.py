""" Views associated with recipe """

from flask import render_template, request, url_for, redirect
from flask_login import login_required
from flask.ext.login import current_user

from app.recipe import recipe
from app.recipe.forms import URLForm, EditRecipeForm, EditRecipeStepForm, EditIngredientForm
from models.core.recipe import Recipe
from operations.helper import url_parse

from operations.recipe import recipe_lookup, recipe_modify, recipe_step_lookup,recipe_step_modify, quantity_lookup, quantity_modify

@recipe.route('/recipe/add', methods=['GET', 'POST'])
@login_required
def add():
    """ Add a Recipe """
    form = URLForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            url_parse.allrecipes(request.form['URL'], current_user.id)
    return render_template('recipe/add_recipe.html', form=form)

@recipe.route('/recipe/view/', methods=['GET'])
@login_required
def view():
    """ View a specific Recipe """
    recipe = recipe_lookup.by_id(request.args.get('recipe_id'))
    return render_template('recipe/view.html', recipe=recipe)


# TODO: Add decorator to ensure user own's this recipe
@recipe.route('/recipe/edit_recipe/', methods=['GET', 'POST'])
@login_required
def edit_recipe():
    """ Edit a Recipe Name """
    form = EditRecipeForm(request.form)
    recipe = recipe_lookup.by_id(request.args.get('recipe_id'))

    if request.method == "POST":
        if form.validate_on_submit():
            recipe_modify.save(recipe, request.form)
            return redirect(url_for('recipe.view', recipe_id=recipe.id))
    else:
        form = EditRecipeForm(obj=recipe)

    return render_template('recipe/edit_recipe.html', var={'form':form, 'recipe_id':recipe.id})



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

    return render_template('recipe/edit_recipe_step.html', var={'form':form, 'recipe_step_id':recipe_step.id})


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

    return render_template('recipe/edit_ingredient.html', var={'form':form, 'quantity_id':ingredient.id})




@recipe.route('/recipe/view_all')
@login_required
def view_all():
    """ View all Recipes """
    all_recipes = recipe_lookup.get_all()

    return render_template('recipe/view_all.html', all_recipes=all_recipes)
