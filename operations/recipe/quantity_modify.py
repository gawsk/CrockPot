""" Provides modification functions for Quantity objects """

from operations import crud

def add(quantity_obj):
    """ Add a Quantity Object to the database """
    crud.add(quantity_obj)
