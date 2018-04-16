""" Contains the Category Model """

from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship
from models.core.recipe_url import RecipeURL
from config import Config


class Category(Config.Base):
    """ Encapsulates an Category  """
    # pylint: disable=C0103
    # pylint: disable=too-few-public-methods

    __tablename__ = 'category'


    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))

    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3

    def __repr__(self):
        return '<Category: {}>'.format(self.name)
