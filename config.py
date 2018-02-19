from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE_CONN = 'mysql://root:root@localhost/crockpot_db'

class Config(object):
    """
    Common configurations
    """
    SA_ENGINE = create_engine(DATABASE_CONN, echo=False)
    SA_BASE = declarative_base(SA_ENGINE)
    SA_SESSION = scoped_session(
    	sessionmaker(
    		bind=SA_ENGINE
    	)
    )

    Base = declarative_base()
    Base.query = SA_SESSION.query_property()



class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True # Debug mode
    SQLALCHEMY_ECHO = True # Helps with debugging sqlalchemy errors

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False




app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
