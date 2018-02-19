"""Contains the SQLAlchemyMiddleware class"""

from operations import query_session



class SQLAlchemyMiddleware(object):
    """ Middleware to ensure database is closed after each request """
    # pylint: disable=too-few-public-methods

    def __init__(self, app):
        """ Initialize Middleware """
        self.app = app

    def __call__(self, environ, start_response):
        """ Ensure database is closed after each request """
        try:
            query_session.get_session().begin_nested
        except BaseException:
            query_session.get_session().rollback()
        finally:
            query_session.get_session().commit()
            query_session.get_session().close()

        return self.app(environ, start_response)
