""" Module provides functions for querying RecipeUrl Objects """

from models.core.recipe import Recipe
from operations import query_session

def by_user_url(user_id, url_id):
    """ Get RecipeURL owned by a user with the url id """

    session = query_session.get_session()
    return session.query(Recipe).filter(Recipe.url_id == url_id) \
                                .filter(Recipe.user_id == user_id) \
                                .first()

def get_all():
    """ Get all RecipeURL's """
    session = query_session.get_session()
    return session.query(Recipe).all()

def by_id(recipe_id):
    """ Get Recipe by Id """
    session = query_session.get_session()
    return session.query(Recipe).filter(Recipe.id == recipe_id).first()
