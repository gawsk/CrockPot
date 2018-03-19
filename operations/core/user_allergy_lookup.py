""" Module provides functions for querying UserAllergy Objects """

from models.core.allergy import Allergy
from models.core.user_allergy import UserAllergy
from operations import query_session

def get_all():
    """ Get all UserAllergies """
    session = query_session.get_session()
    return session.query(UserAllergy).all()


def by_user_allergy(user_id, allergy_id):
    """ Get an allergy owned by a user """
    session = query_session.get_session()

    return session.query(UserAllergy).filter(UserAllergy.user_id == user_id) \
                                     .filter(UserAllergy.allergy_id == allergy_id) \
                                     .first()
