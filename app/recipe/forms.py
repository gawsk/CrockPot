""" Forms for auth """

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Email
from operations.core import user_lookup
from flask import flash


class URLForm(FlaskForm):
    """ Form to ask user for URL to use """

    URL = TextField('URL')
    submit = SubmitField('Submit')

    # def validate(self):
    #     """ Validation to ensure url is entered """
    #     return len(URL) > 0 and URL is not None
