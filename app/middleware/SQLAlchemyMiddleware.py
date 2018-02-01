"""Contains the SQLAlchemyMiddleware class"""

from operations import query_session


# TODO: Figure out why this won't work... This is crucial
class SQLAlchemyMiddleware(object):
	""" Middleware to ensure database is closed after each request """

	def __init__(self, app):
		self.app = app


	def __call__(self, environ, start_response):
	    try:
	        query_session().begin_nested()
	        return self.app(environ, start_response)
	    except BaseException:
	        query_session.rollback()
	        query_session.close()
	    finally:
	        query_session().commit()
	
	#
	# def process_response(self, request, response):
	# 	""" Close and commit the Database session"""
	# 	session = query_session.get_session()
	# 	session.commit()
	# 	session.close()
	# 	return response
	#
	# def process_exception(self, *unused):
	# 	""" Handler for exception; rollback and close the session """
	# 	session = query_session.get_session()
	# 	session.rollback()
	# 	session.close()
