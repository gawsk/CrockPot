
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os, sys
sys.path.append("../") #Add hte root dir to the path
from app import *
import unittest

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


TEST_DB = 'mysql://root:root@localhost/crockpot_db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):


        # Initialize SQL server
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass


########################################################
#################### tests #############################
########################################################

    #Test the MAIN page to ensure it loads
    def test_main_page(self):
        print "\nTEST - Load Main Page...",
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print "PASSED",


    #Test the REGISTER page to ensure it loads
    def test_register_page(self):
        print "\nTEST - Load Register Page...",
        response = self.app.get('/register', follow_redirects=True)
        result = self.assertEqual(response.status_code, 200)
        print "PASSED",




if __name__ == "__main__":
    unittest.main()
