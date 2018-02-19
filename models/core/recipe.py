""" Contains the Recipe Model """

from sqlalchemy import Column, BigInteger, String, ForeignKey
from models.core.user import User
from config import Config


class Recipe(Config.Base):
    """ Encapsulates a Recipe, it contains the user_id it belongs to """
    # pylint: disable=C0103
    # pylint: disable=too-few-public-methods

    __tablename__ = 'recipe'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200))
    description = Column(String(500))
    user_id = Column(BigInteger, ForeignKey(User.id))


    def __repr__(self):
        return '<Recipe: {}>'.format(self.name)