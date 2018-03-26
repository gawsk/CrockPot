""" App module provides the setup for the entire application """

# Third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_bootstrap import Bootstrap


# Local imports
from config import app_config
from app.middleware.SQLAlchemyMiddleware import SQLAlchemyMiddleware


# Variable initializations
login_manager = LoginManager() # pylint: disable=C0103

def create_app(config_name):
    """ Create the core of the application """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.static_folder = 'static'

    app.wsgi_app = SQLAlchemyMiddleware(app.wsgi_app)

    #pylint: disable=unused-variable
    bootstrap = Bootstrap(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.recipe import recipe as recipe_blueprint
    app.register_blueprint(recipe_blueprint)

    from app.user_management import user_mgmt as user_mgmt_blueprint
    app.register_blueprint(user_mgmt_blueprint)

    return app
