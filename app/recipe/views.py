""" Views associated with recipe """

from flask import render_template, request
from flask_login import login_required
from flask.ext.login import current_user

from app.recipe import recipe
from app.recipe.forms import URLForm

from operations.recipe import url_parse

from operations.recipe import recipe_lookup, ingredient_lookup

@recipe.route('/recipe/add',  methods=['GET', 'POST'])
@login_required
def add():
    """ Add a Recipe """
    form = URLForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            url_parse.allrecipes(request.form['URL'], current_user.id)
    return render_template('recipe/add_recipe.html', form=form)


@recipe.route('/recipe/view')
@login_required
def view():
    """ View all Recipes """
    all_recipes = recipe_lookup.get_all()
    print all_recipes
    print ingredient_lookup.get_all()


    return render_template('recipe/view.html', all_recipes=all_recipes)
