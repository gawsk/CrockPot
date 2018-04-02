""" Forms for searching """

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, validators
from wtforms.fields import StringField
from wtforms.widgets import TextArea


class SearchForm(FlaskForm):
    """ Form to search an ingredient """
    name = TextField("Name", [validators.Length(min=1, max=200), validators.DataRequired()])
    submit = SubmitField('Submit')
