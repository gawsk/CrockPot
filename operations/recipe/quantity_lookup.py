""" Module provides functions for querying Quantity Objects """

from models.core.quantity import Quantity
from operations import query_session

def by_id(quantity_id):
    """ Get Quantity by its id  """

    session = query_session.get_session()
    return session.query(Quantity).filter(Quantity.id == quantity_id).first()
