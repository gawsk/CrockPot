""" Provides modification functions for Measurement objects """

from operations import crud

def add(measurement_obj):
    """ Add a Measurement Object to the database """
    crud.add(measurement_obj)

def delete(measurement_obj):
    """ Delete a Measurement Object """
    crud.delete(measurement_obj)
