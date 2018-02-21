""" Provides modification functions for Measurement objects """

from operations import crud

def add(measurement_obj):
    """ Add a Measurement Object to the database """
    crud.add(measurement_obj)
