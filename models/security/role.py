""" Contains the Role model class """
from sqlalchemy import Column, Integer, String
from config import Config



class Role(Config.Base):
    """ Role is used to determine what security permission a user has """
    # pylint: disable=C0103
    # pylint: disable=too-few-public-methods

    __tablename__ = 'role'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), unique=True)


    SUPERADMIN = 1
    USER = 2


    def __repr__(self):
        return '<Role: {}>'.format(self.name)
