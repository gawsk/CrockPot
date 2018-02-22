""" Module provides helper functions for Quantity """

from operations.recipe import ingredient_lookup, recipe_lookup, measurement_modify, measurement_lookup, ingredient_modify
from models.core.ingredient import Ingredient
from models.core.measurement import Measurement


def parse(description):
    """ Parse an ingredient text and insert into measurement/ingredients tables """
    measurements = {'teaspoons', 'tablespoons', 'cup', 'cups', 'pints', 'pint', 'quarts', 'quart', \
                        'ounce', 'ounces', 'dash', 'pinch', 'cube', 'cubes'}

    description = description.split(' ')
    quantity = description[0].encode('utf8')
    measurement, increments = None, None

    if description[1] in measurements:
        increments = description[1]
        description = ' '.join(description[2:])
        measurement = measurement_lookup.by_name(increments)
    else:
        description = ' '.join(description[1:])

    ingredient = ingredient_lookup.by_name(description)
    if ingredient is None:
        ingredient_modify.add(Ingredient(name=description))
        ingredient = ingredient_lookup.by_name(description)

    if measurement is None and increments != None:
        measurement_modify.add(Measurement(name=increments))
        measurement = measurement_lookup.by_name(increments)

    if not measurement:
        measurement = None
    else:
        measurement = measurement.id

    return ingredient.id, measurement, quantity
