""" Contains the Recipe Model """

from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from models.core.user import User
from config import Config


class Recipe(Config.Base):
    """ Encapsulates a Recipe, it contains the user_id it belongs to """
    __tablename__ = 'recipe'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(200))
    description = Column(String(500))
    user_id = Column(BigInteger, ForeignKey(User.id))



    def __repr__(self):
        return '<Recipe: {}>'.format(self.name)
