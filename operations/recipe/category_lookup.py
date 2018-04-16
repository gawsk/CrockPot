""" Module provides functions for querying Category Objects """

from models.core.category import Category
from operations import query_session

def get_all():
    """ Get all categories """
    session = query_session.get_session()
    return session.query(Category).all()
