""" Views associated with recipe """

from flask import render_template, request
from flask_login import login_required
from flask.ext.login import current_user

from app.recipe import recipe
from app.recipe.forms import URLForm

from operations.helper import url_parse

from operations.recipe import recipe_lookup

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


@recipe.route('/recipe/view_all')
@login_required
def view_all():
    """ View all Recipes """
    all_recipes = recipe_lookup.get_all()

    return render_template('recipe/view_all.html', all_recipes=all_recipes)
