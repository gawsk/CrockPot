""" Views associated with recipe """

from flask import render_template, request, url_for, redirect
from flask_login import login_required
from flask.ext.login import current_user

from app.recipe import recipe
from app.recipe.forms import URLForm, EditRecipe
from models.core.recipe import Recipe
from operations.helper import url_parse

from operations.recipe import recipe_lookup, recipe_modify

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
@recipe.route('/recipe/edit/', methods=['GET', 'POST'])
@login_required
def edit():
    """ Edit a Recipe Name """
    form = EditRecipe(request.form)
    recipe = recipe_lookup.by_id(request.args.get('recipe_id'))

    if request.method == "POST":
        if form.validate_on_submit():
            recipe_modify.save(recipe, request.form)
            return redirect(url_for('recipe.view', recipe_id=recipe.id))
    else:
        form = EditRecipe(obj=recipe)

    return render_template('recipe/edit_recipe.html', var={'form':form, 'recipe_id':recipe.id})


@recipe.route('/recipe/view_all')
@login_required
def view_all():
    """ View all Recipes """
    all_recipes = recipe_lookup.get_all()

    return render_template('recipe/view_all.html', all_recipes=all_recipes)
