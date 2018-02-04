""" Forms for auth """

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from models.core.user import User
from operations.core import user_lookup
from flask import flash


class RegistrationForm(FlaskForm):
    """ Form to create an account """

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate(self):
        """ Validation to ensure no duplicates """
        username = user_lookup.by_username(self.username.data)
        if username is not None:
            flash("Username taken already")

        email = user_lookup.by_email(self.email.data)
        if email is not None:
            flash("Email taken already")

class LoginForm(FlaskForm):
    """ Form for users to login """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
