
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
#################### TESTS #############################
########################################################


########################
## TEST FOR PAGE LOAD ##
##  (NOT LOGGED IN)   ##
########################

    #Test the MAIN page to ensure it loads
    def test_01_01_main_page(self):
        print "\nTEST - Load Main Page...",
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print "PASSED",


    #Test the REGISTER page to ensure it loads
    def test_01_02_register_page(self):
        print "\nTEST - Load Register Page...",
        response = self.app.get('/register', follow_redirects=True)
        result = self.assertEqual(response.status_code, 200)
        print "PASSED",


    #Test the LOGIN page to ensure it loads
    def test_01_03_login_page(self):
        print "\nTEST - Load Login Page...",
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print "PASSED",


    #Test the DASHBOARD page to ensure it loads
    #  Actually this redirects to the login page, and gives you a message
    #    that says, "You must be logged in to access this page. "
    def test_01_04_dashbaord_page(self):
        print "\nTEST - Load Dashboard Page...",
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print "PASSED",


########################
## TEST FOR PAGE LOAD ##
##     (LOGGED IN)    ##
########################

    #Test the Login page with a Email and Password
    '''
    def test_02_01_dashbaord_page(self):
        print "\nTEST - Load Login Page...",
        response = self.app.post('/login', {'email': 'test@rpi.edu', 'password': 'teast', 'submit': 'Login'})
        #response = self.app.get('/login', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        print "PASSED",
    '''













    ##LEAVE THIS LAST
    #DUMMY TEST to make print statements in terminal display correct
    def test_99_01_dummyTest_page(self):
        self.assertEqual("!", "!")
        print


if __name__ == "__main__":
    unittest.main()
