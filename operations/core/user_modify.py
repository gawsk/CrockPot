""" Provides modification functions for User objects """

from operations import crud
from models.core.user import User

def add(user_obj):
    """Add a User"""
    user_obj.set_password()
    return crud.add(user_obj)

def save(user_id, form):
    """ Save a User with new form data """
    session = crud.pre_save()
    values = form.to_dict()
    del values['csrf_token']
    del values['submit']
    session.query(User).filter(User.id == user_id) \
                           .update(values)

    crud.save_update(session)




def delete(user_obj):
    """Delete a User"""
    return crud.delete(user_obj)
