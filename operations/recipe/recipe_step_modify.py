""" Provides modification functions for Recipe Step objects """

from operations import crud
from models.core.recipe_step import RecipeStep

def add(recipe_step_obj):
    """ Add a Recipe Step Object to the database """
    crud.add(recipe_step_obj)


def save(recipe_step_obj, form):
    """ Save a recipe step from a form """
    session = crud.pre_save()
    values = form.to_dict()
    del values['csrf_token']
    del values['submit']
    session.query(RecipeStep).filter(RecipeStep.id == recipe_step_obj.id).update(values)

    crud.save_update(session)
