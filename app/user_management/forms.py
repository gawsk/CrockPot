""" Forms for User Management """

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, validators
from wtforms.fields import StringField, SelectField
from wtforms.widgets import TextArea


class EditUserForm(FlaskForm):
    """ Form to edit a User """

    name = StringField("Name", [validators.Length(min=0, max=45), validators.DataRequired()])
    email = StringField("Email", [validators.Length(min=1, max=320), validators.Email()])
    username = StringField("Username", [validators.Length(min=1, max=45)])
    submit = SubmitField('Submit')



class AddAllergyForm(FlaskForm):
    """ Form to edit an Allergy owned by a user """
    allergy_id = SelectField("Allergy", coerce=int )
    submit = SubmitField('Submit')
