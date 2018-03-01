""" Module provides functions for querying Allergy Objects """

from models.core.allergy import Allergy
from operations import query_session

def get_all():
    """ Get all ingredients """
    session = query_session.get_session()
    return session.query(Allergy).all()
