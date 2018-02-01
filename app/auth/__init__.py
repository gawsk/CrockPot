""" Auth module provides endpoints for Registration/Logging in a User """

from flask import Blueprint

auth = Blueprint('auth', __name__)

from app.auth import views
