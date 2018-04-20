""" Contains the Allergy Model """

from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship
from models.core.recipe_url import RecipeURL
from config import Config


class Allergy(Config.Base):
    """ Encapsulates an Allergy  """

    __tablename__ = 'allergy'


    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))

    MILK = 1
    PEANUTS = 2
    EGG = 3
    NUTS = 4
    SOY = 5
    WHEAT = 6
    FISH = 7
    SHELLFISH = 8
    CORN = 9
    GELATIN = 10
    SESAME = 11
    SUNFLOWER = 12
    POPPY = 13


    def __repr__(self):
        return '<Allergy: {}>'.format(self.name)
