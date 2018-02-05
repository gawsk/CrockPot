""" Provides modification functions for User objects """

from operations import crud

def add(user_obj):
    """Add a User"""
    return crud.add(user_obj)

def save(user_obj):
    """Save all User objects that have been edited in this Session"""
    return crud.save(user_obj)

def delete(user_obj):
    """Delete a User"""
    return crud.delete(user_obj)
