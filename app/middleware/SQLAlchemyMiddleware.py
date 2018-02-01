"""Contains the SQLAlchemyMiddleware class"""

from operations import query_session



class SQLAlchemyMiddleware:
	""" Middleware to ensure database is closed after each request """

	def __init__(self, app):
		self.app = app


	def __call__(self, environ, start_response):
		try:
			query_session.get_session().begin_nested
		except BaseException:
			query_session.get_session().rollback()
		finally:
			query_session.get_session().commit()
			query_session.get_session().close()

		return self.app(environ, start_response)
