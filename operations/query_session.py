""" Module used to get a handle to the DB session """

from config import Config

def get_session():
    """Get a handle to the DB session"""
    return Config.SA_SESSION()
