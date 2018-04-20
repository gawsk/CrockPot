""" Contains the UserAllergy Model """

from sqlalchemy import Column, BigInteger, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship
from models.core.allergy import Allergy
from config import Config



class UserAllergy(Config.Base):
    """ Encapsulates a User's Allergy  """

    __tablename__ = 'user_allergy'

    allergy_id = Column(BigInteger, ForeignKey(Allergy.id), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.id'), primary_key=True)

    allergy = relationship("Allergy")

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

    @property
    def name(self):
        """ Return the name of the allergy """
        return self.allergy.name

    def __repr__(self):
        return '<UserAllergy: {}>'.format(self.name)
