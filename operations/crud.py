""" Simple CRUD operations """

from operations import query_session

def add(obj):
    """Add a new Object"""
    session = query_session.get_session()
    session.begin_nested()

    session.add(obj)
    session.flush()
    session.commit()

def pre_save():
    """pre_save an Object that has been edited in this Session"""
    session = query_session.get_session()
    session.begin_nested()
    return session
    # session.save(obj)
    # session.commit()

def save(obj):
    """ Save an Object that has been edited in this session """
    session = query_session.get_session()
    session.begin_nested()

    session.save(obj)
    session.commit()

def save_update(session):
    """ Commit update changes in a given session """
    session.commit()




def delete(obj):
    """Delete an Object"""
    session = query_session.get_session()
    session.begin_nested()

    session.delete(obj)
    session.commit()
