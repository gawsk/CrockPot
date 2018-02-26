""" Module provides functions for querying RecipeUrl Objects """

from models.core.recipe_url import RecipeURL
from operations import query_session

def by_url(url):
    """ Get RecipeURL by url """

    session = query_session.get_session()
    return session.query(RecipeURL).filter(RecipeURL.url == url).first()


def by_user_url(user_id, url_id):
    """ Get RecipeURL owned by a user with the url id """

    session = query_session.get_session()
    return session.query(Recipe).filter(Recipe.url_id == url_id) \
                                .filter(Recipe.user_id == user_id) \
                                .first()
