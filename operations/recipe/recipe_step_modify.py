""" Provides modification functions for Recipe Step objects """

from operations import crud

def add(recipe_step_obj):
    """ Add a Recipe Step Object to the database """
    crud.add(recipe_step_obj)
