""" Module provides functions for querying Users """

from models.core.user import User

def by_email(email):
    """ Get User by email """
    return User.query.filter(User.email==email).first()

def by_id(user_id):
    """ Get User by id """
    return User.query.filter(User.id==user_id).first()
