""" Search module provides endpoints for searching recipes """

from flask import Blueprint

search = Blueprint('search', __name__) # pylint: disable=C0103

from app.search import views #pylint: disable=C0413
