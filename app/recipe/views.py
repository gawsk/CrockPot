""" Views associated with recipe """

from flask import render_template, request
from flask_login import login_required

from app.recipe import recipe
from app.recipe.forms import URLForm

from lxml import html
from operations.recipe import url_parse

@recipe.route('/recipe/add',  methods=['GET', 'POST'])
def add():
    """ Home Page """
    form = URLForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            url_parse.allrecipes(request.form['URL'])
    return render_template('recipe/add_recipe.html', form=form)
