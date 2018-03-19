""" User Management module provides endpoints for the managing a User """

from flask import Blueprint

user_mgmt = Blueprint('user_mgmt', __name__) # pylint: disable=C0103

from app.user_management import views #pylint: disable=C0413
