""" Provides modification functions for Ingredient objects """

from operations import crud
def add(ingredient_obj):
    """ Add a Ingredient Object to the database """
    crud.add(ingredient_obj)
