""" Recipe module provides endpoints for the creating/editing recipes """

from flask import Blueprint

recipe = Blueprint('recipe', __name__) # pylint: disable=C0103

from app.recipe import views #pylint: disable=C0413
