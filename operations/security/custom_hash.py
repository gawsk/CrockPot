""" Module provides functions for generating password hashs """

import hashlib

def create(username, password):
    """ Create a hashed string of a password with username as the salt """
    return hashlib.sha512(username + password).hexdigest()
