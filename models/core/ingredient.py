""" Contains the Ingredient Model """

from sqlalchemy import Column, BigInteger, String
from config import Config


class Ingredient(Config.Base):
    """ Encapsulates an Ingredient """

    __tablename__ = 'ingredient'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(130))


    def __repr__(self):
        return '<Ingredient: {}>'.format(self.name)
