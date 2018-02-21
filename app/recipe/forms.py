""" Forms for auth """

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, HiddenField, validators


class URLForm(FlaskForm):
    """ Form to ask user for URL to use """

    URL = TextField('URL')
    submit = SubmitField('Submit')

    # def validate(self):
    #     """ Validation to ensure url is entered """
    #     return len(URL) > 0 and URL is not None


class EditRecipe(FlaskForm):
    """ Form to edit a Recipe name """
    name = TextField("Name", [validators.Length(min=1, max=200)])
    description = TextField("Description", [validators.Length(min=1, max=500)])
    submit = SubmitField('Submit')
