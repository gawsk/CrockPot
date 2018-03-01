""" Module provides functions for querying Users """

from models.core.user import User
from operations import query_session

def by_email(email):
    """ Get User by email """

    session = query_session.get_session()
    return session.query(User).filter(User.email == email).first()

def by_id(user_id):
    """ Get User by id """

    session = query_session.get_session()
    return session.query(User).filter(User.id == user_id).first()

def by_username(username):
    """ Get User by username """

    session = query_session.get_session()
    return session.query(User).filter(User.username == username).all()

def get_all():
    """ Get all User objects """

    session = query_session.get_session()
    return session.query(User).all()
