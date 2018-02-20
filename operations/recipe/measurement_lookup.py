""" Module provides functions for querying Measurement Objects """

from models.core.measurement import Measurement
from operations import query_session

def by_name(name):
    """ Get Measurement by its name  """

    session = query_session.get_session()
    return session.query(Measurement).filter(Measurement.name == name).first()
