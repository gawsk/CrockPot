""" Contains the Quantity Step Model """

from sqlalchemy import Column, BigInteger, String, ForeignKey, Text, Integer
from models.core.recipe import Recipe
from models.core.measurement import Measurement
from models.core.ingredient import Ingredient
from config import Config


class Quantity(Config.Base):
    """ Encapsulates a Quantity that beloings to a recipe """
    # pylint: disable=C0103
    # pylint: disable=too-few-public-methods

    __tablename__ = 'quantity'

    id = Column(BigInteger, primary_key=True)
    recipe_id = Column(BigInteger, ForeignKey(Recipe.id))
    ingredient_id = Column(BigInteger, ForeignKey(Ingredient.id))
    measurement_id = Column(BigInteger, ForeignKey(Measurement.id))
    amount = Column(Integer)


    def __repr__(self):
        return '<Quantity: {}>'.format(self.name)
