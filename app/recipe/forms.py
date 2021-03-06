""" Forms for recipe """

from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, validators, SelectField
from wtforms.fields import StringField
from wtforms.widgets import TextArea

class URLForm(FlaskForm):
    """ Form to ask user for URL to use """
    choices = [
        ('1', 'Breakfast'),
        ('2', 'Lunch'),
        ('3', 'Dinner')
    ]

    URL = TextField('URL')
    category_id = SelectField("Category", choices=choices)
    submit = SubmitField('Submit')

    # def validate(self):
    #     """ Validation to ensure url is entered """
    #     return len(URL) > 0 and URL is not None


class EditRecipeForm(FlaskForm):
    """ Form to edit a Recipe name """
    name = TextField("Name", [validators.Length(min=1, max=200)])
    description = StringField("Description", [validators.Length(min=0, max=500)], widget=TextArea())
    submit = SubmitField('Submit')


class EditRecipeStepForm(FlaskForm):
    """ Form to edit a RecipeStep """
    description = StringField("Description", widget=TextArea())
    submit = SubmitField('Submit')


class EditIngredientForm(FlaskForm):
    """ Form to edit an Ingredient """
    description = TextField("Description", [validators.Length(min=5, max=100)])
    submit = SubmitField('Submit')
