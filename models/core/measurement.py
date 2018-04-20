""" Contains the Measurement Model """

from sqlalchemy import Column, BigInteger, String
from config import Config


class Measurement(Config.Base):
    """ Encapsulates a Measurement """

    __tablename__ = 'measurement'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return '<Measurement: {}>'.format(self.name)
