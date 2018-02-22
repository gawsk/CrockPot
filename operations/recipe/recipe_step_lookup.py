""" Module provides functions for querying RecipeStep Objects """

from models.core.recipe_step import RecipeStep
from operations import query_session

def by_id(recipe_step_id):
    """ Get RecipeStep by url """

    session = query_session.get_session()
    return session.query(RecipeStep).filter(RecipeStep.id == recipe_step_id).first()
