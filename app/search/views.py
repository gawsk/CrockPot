""" Views associated with search """

from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required
from flask.ext.login import current_user

from app.search import search
from app.search.forms import SearchForm
from config import Config
from sqlalchemy import text

@search.route('/search/', methods=['POST'])
@login_required
def ingrd():
    """ Search an Ingredient and show results"""
    form = SearchForm(request.form)
    results = None
    if request.method == "POST":
        if form.validate_on_submit():
            ingredient = form.name.data
            results = like_ingredient_name(ingredient)
    return render_template('search/results.html', var={'form':form, 'results':results})



def like_ingredient_name(ingredient_name):
    """ Get all recipes with a name like the ingredient given """
    query = """
        SELECT r.* FROM recipe r JOIN
            (SELECT q.* FROM quantity q JOIN
                (SELECT i.id as ingredient_id FROM ingredient i WHERE i.name LIKE '%{ingrd}%')
            i ON q.ingredient_id = i.ingredient_id)
        q ON r.id = q.recipe_id
        GROUP BY r.id
    """.format(ingrd=ingredient_name)
    return Config.SA_ENGINE.execute(text(query))
