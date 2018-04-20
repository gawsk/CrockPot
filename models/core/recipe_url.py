""" Contains the Recipe URL Model """

from sqlalchemy import Column, BigInteger, String
from config import Config


class RecipeURL(Config.Base):
    """ Encapsulates a Recipe URL, it contains url a recipe is from """

    __tablename__ = 'recipe_url'

    id = Column(BigInteger, primary_key=True)
    url = Column(String(1000)) # 1000 should be enough for now

    def __repr__(self):
        return '<RecipeURL: {}>'.format(self.name)
