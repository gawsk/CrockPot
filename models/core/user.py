""" Contains the User model class """

from flask_login import UserMixin
from app import login_manager
from config import Config
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from models.security.role import Role
from operations.security import custom_hash


class User(Config.Base, UserMixin):
    """ A User is used to keep information specifics """
    # pylint: disable=C0103

    __tablename__ = 'user'

    id = Column('id', BigInteger, primary_key=True)
    email = Column('email', String(320), unique=True)
    name = Column('name', String(45), nullable=True)
    username = Column('username', String(45), unique=True)
    password = Column('password', String(150))
    role_id = Column('role_id', Integer, ForeignKey(Role.id), default=Role.USER)


    def set_password(self):
        """ Store the password hashed """
        self.password = custom_hash.create(self.username, self.password)

    def verify_password(self, password):
        """ Check if the password matches """
        return custom_hash.create(self.username, password) == self.password

    def __repr__(self):
        return '<User: {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    """ Load the user object for Login """
    # pylint: disable=maybe-no-member
    return User.query.get(user_id)
