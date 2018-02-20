""" Contains the Ingredient Model """

from sqlalchemy import Column, BigInteger, String
from config import Config


class Ingredient(Config.Base):
    """ Encapsulates an Ingredient """
    # pylint: disable=C0103
    # pylint: disable=too-few-public-methods

    __tablename__ = 'ingredient'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(130))


    def __repr__(self):
        return '<Ingredient: {}>'.format(self.name)
