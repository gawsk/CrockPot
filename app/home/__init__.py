""" Home module provides endpoints for the homepage and the like """

from flask import Blueprint

home = Blueprint('home', __name__) # pylint: disable=C0103

from app.home import views #pylint: disable=C0413
