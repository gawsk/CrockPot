""" Module provides functions for querying UserAllergy Objects """

from models.core.allergy import Allergy
from models.core.user_allergy import UserAllergy
from operations import query_session

def get_all():
    """ Get all UserAllergies """
    session = query_session.get_session()
    return session.query(Allergy).all()
