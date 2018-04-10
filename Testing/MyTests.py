
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os, sys
sys.path.append("../") #Add hte root dir to the path
from app import *
import unittest

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)


TEST_DB = 'mysql://root:root@localhost/crockpot_db'

testuser_email = "test@rpi.edu"
testuser_password = "test"
testURL_INVALID = "http://www.youtube.com/"
testURL_VALID = "https://www.allrecipes.com/recipe/84000/sicilian-pineapple-pork-roast/"



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

    '''
    #Test the DASHBOARD page to ensure it loads
    #  Actually this redirects to the login page, and gives you a message
    #    that says, "You must be logged in to access this page. "
    def test_01_04_dashboard_page(self):
        print "\nTEST - Load Dashboard Page...",
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print "PASSED",
    '''


########################
## TEST FOR PAGE LOAD ##
##     (LOGGED IN)    ##
########################

    #Test the Login page with a Email and Password and can reach page behind login wall
    #  REQUIRES Prior Registration
    def test_02_01_login_test(self):
        print "\nTEST - User Login Page...",

        #Send Login Post
        response = self.app.post('/login', data={'email': testuser_email, 'password': testuser_password, 'submit': 'Login'}, follow_redirects=False)

        #Try to access view_all recipes (Behind login wall)
        response = self.app.get('/recipe/view_all', follow_redirects=False)

        #Check that we can access the page behind the login wall
        self.assertEqual(response.status_code, 200)
        print "PASSED",


    #Test the Login page with a Email and Password
    def test_02_02_login_failed_test(self):
        print "\nTEST - User Login Page - Failed...",

        #Send Login Post
        response1 = self.app.post('/login', data={'email': testuser_email, 'password': 'BAD_PASSWORD', 'submit': 'Login'}, follow_redirects=False)

        #Try to access view_all recipes (Behind login wall)
        response2 = self.app.get('/recipe/view_all', follow_redirects=False)

        #Check that we can NOT access the page behind the login wall
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        print "PASSED",

    #Test that when logged in, we can reach the home page
    def test_02_03_login_reach_home_test(self):
        print "\nTEST - User Login - Reach Home...",

        #Send Login Post
        response1 = self.app.post('/login', data={'email': testuser_email, 'password': testuser_password, 'submit': 'Login'}, follow_redirects=False)

        #Try to access view_all recipes (Behind login wall)
        response2 = self.app.get('/', follow_redirects=False)

        #Check that we can access the page behind the login wall
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response2.status_code, 200)
        print "PASSED",

    #Test that when logged in, we can reach the add recipe
    def test_02_04_login_reach_add_recipe_test(self):
        print "\nTEST - User Login - Reach Add Recipe....",

        #Send Login Post
        response1 = self.app.post('/login', data={'email': testuser_email, 'password': testuser_password, 'submit': 'Login'}, follow_redirects=False)

        #Try to access view_all recipes (Behind login wall)
        response2 = self.app.get('/recipe/add', follow_redirects=False)

        #Check that we can access the page behind the login wall
        self.assertEqual(response1.status_code, 302)
        self.assertEqual(response2.status_code, 200)
        print "PASSED",



########################
## TEST FOR ADD RECIPE##
##     (LOGGED IN)    ##
########################

    #Test the Add Recipe page - Should be invalid URL
    def test_03_01_AddRecipe_invalid_URL(self):
        print "\nTEST - Add Recipe INVALID URL Page...",

        #Send Login Post
        response = self.app.post('/login', data={'email': testuser_email, 'password': testuser_password, 'submit': 'Login'}, follow_redirects=False)

        #Try to post
        response = self.app.post('/recipe/add', data={'URL': testURL_INVALID, 'submit': 'Submit'}, follow_redirects=False)

        #Check that we have reached an invalid URL
        self.assertEqual(response.status_code, 200)
        print "PASSED",

    #Test the Add Recipe page - Should be valid URL
    def test_03_02_AddRecipe_valid_URL(self):
        print "\nTEST - Add Recipe VALID URL Page...",

        #Send Login Post
        response = self.app.post('/login', data={'email': testuser_email, 'password': testuser_password, 'submit': 'Login'}, follow_redirects=False)

        #Try to access add recipes (Behind login wall)
        response = self.app.post('/recipe/add', data={'URL': testURL_VALID, 'submit': 'Submit'}, follow_redirects=False)

        #Check that we have reached an invalid URL
        self.assertEqual(response.status_code, 200)
        print "PASSED",












    ##LEAVE THIS LAST
    #DUMMY TEST to make print statements in terminal display correct
    def test_99_01_dummyTest_page(self):
        self.assertEqual("!", "!")
        print


if __name__ == "__main__":
    unittest.main()
