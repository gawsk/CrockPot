""" Module provides functions for querying Users """

from models.core.user import User

def by_email(email):
    """ Get User by email """
    return User.query.filter(User.email==email).first()

def by_id(user_id):
    """ Get User by id """
    return User.query.filter(User.id==user_id).first()

def by_username(username):
    """ Get User by username """
    return User.query.filter(User.username==username).first()

def get_all():
    """ Get all User objects """
    return User.query.all()
