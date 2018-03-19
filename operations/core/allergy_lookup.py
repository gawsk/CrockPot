""" Module provides functions for querying Allergy Objects """

from models.core.allergy import Allergy
from models.core.user_allergy import UserAllergy
from operations import query_session
from sqlalchemy.orm import load_only

def get_all():
    """ Get all Allergies """
    session = query_session.get_session()
    return session.query(Allergy).all()


def get_user_allergies(user_id):
    """ Get all Allergies that a user owns """
    session = query_session.get_session()

    return session.query(UserAllergy).filter(UserAllergy.user_id == user_id).all()


def get_non_allergies(allergies):
    """ Get all allergies that aren't part of a list """
    session = query_session.get_session()

    return session.query(Allergy).filter(~Allergy.id.in_(allergies)).all()
