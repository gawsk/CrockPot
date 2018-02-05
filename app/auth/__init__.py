""" Auth module provides endpoints for Registration/Logging in a User """

from flask import Blueprint

auth = Blueprint('auth', __name__) # pylint: disable=C0103

from app.auth import views #pylint: disable=C0413
