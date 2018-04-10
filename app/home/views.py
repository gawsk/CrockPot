""" Views associated with home """

from flask import render_template
from flask_login import login_required

from app.home import home
from operations.core import user_lookup
from operations.recipe import recipe_lookup

@home.route('/')
def index():
    """ Home Page """
    # Get 8 random recipes
    recipes = recipe_lookup.get_random(8)
    recipes = [recipes[:4], recipes[4:]]

    return render_template('home/index.html', recipes=recipes)
