""" Home module provides endpoints for the homepage and the like """

from flask import Blueprint

home = Blueprint('home', __name__)

from app.home import views
