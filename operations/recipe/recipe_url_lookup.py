""" Module provides functions for querying RecipeUrl Objects """

from models.core.recipe_url import RecipeURL
from operations import query_session

def by_url(url):
    """ Get RecipeURL by url """

    session = query_session.get_session()
    return session.query(RecipeURL).filter(RecipeURL.url == url).first()
