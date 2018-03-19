""" Contains the Quantity Model """

from sqlalchemy import Column, BigInteger, ForeignKey, Integer
from sqlalchemy.orm import relationship
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

    ingredient_obj = relationship("Ingredient")
    measurement_obj = relationship("Measurement")


    def __repr__(self):
        return '<Quantity: {}>'.format(self.id)

    def description(self):
        """ Pretty print of full description """
        desc = [self.amount]
        if self.measurement_id:
            desc.append(self.measurement_obj.name)
        desc.append(self.ingredient_obj.name)
        return ' '.join(desc)
