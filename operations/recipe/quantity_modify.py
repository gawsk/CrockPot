""" Provides modification functions for Quantity objects """

from operations import crud
from models.core.quantity import Quantity
from operations.recipe import ingredient_lookup, recipe_lookup
from operations.helper import quantity_helper

def add(quantity_obj):
    """ Add a Quantity Object to the database """
    crud.add(quantity_obj)


def save(quantity_obj, form):
    """ Save a Quantity from a form """
    session = crud.pre_save()
    form_values = form.to_dict()

    ingredient, measurement, amount = quantity_helper.parse(form_values['description'])

    values = {
        'ingredient_id': ingredient,
        'measurement_id': measurement,
        'amount': amount
    }

    session.query(Quantity).filter(Quantity.id == quantity_obj.id) \
                           .update(values)

    crud.save_update(session)
