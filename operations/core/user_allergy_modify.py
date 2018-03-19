""" Provides modification functions for UserAllergy objects """

from operations import crud
from models.core.user_allergy import UserAllergy

def add(user_id, form):
    """Add a UserAllergy"""
    user_allergy_obj = UserAllergy()

    user_allergy_obj.user_id = user_id
    user_allergy_obj.allergy_id = form['allergy_id']
    return crud.add(user_allergy_obj)

def delete(user_allergy_obj):
    """Delete a UserAllergy"""
    return crud.delete(user_allergy_obj)
