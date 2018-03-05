""" Module provides functions for querying RecipeUrl Objects """

from models.core.recipe import Recipe
from operations import query_session


def by_user_recipe_id(user_id, recipe_id):
    """ Get Recipe owned by a user  """

    session = query_session.get_session()
    return session.query(Recipe).filter(Recipe.id == recipe_id) \
                                .filter(Recipe.user_id == user_id) \
                                .first()

def by_user_url_id(user_id, recipe_url_id):
    """ Get Recipe owned by a user  """

    session = query_session.get_session()
    return session.query(Recipe).filter(Recipe.url_id == recipe_url_id) \
                                .filter(Recipe.user_id == user_id) \
                                .first()


def get_all(user_id):
    """ Get all Recipes owned by a user """
    session = query_session.get_session()

    return session.query(Recipe).filter(Recipe.user_id == user_id).all()

def by_id(recipe_id):
    """ Get Recipe by Id """
    session = query_session.get_session()
    return session.query(Recipe).filter(Recipe.id == recipe_id).first()
