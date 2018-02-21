""" Provides modification functions for RecipeUrl objects """

from operations import crud
from models.core.recipe_url import RecipeURL

def add(url):
    """Add a RecipeURL"""
    recipe_url_obj = RecipeURL(url=url)
    return crud.add(recipe_url_obj)
