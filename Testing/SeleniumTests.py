from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re
import time
import random
import urllib2

flag_isFirstRun = False
recipeURL = ""
localURL = ""

class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.flag_isFirstRun = flag_isFirstRun
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #USER REGISTER TEST CASES
    #
    # Must start with 'test_'
    # TC1.1 - UserRegister [Valid registration]
    def test_01_01_Register_Valid(self):
        print "\n TEST - TC1.1 - UserRegister [Valid registration]...",
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element_by_xpath("//div[@onclick='w3_open()']").click()
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("test")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        URL = driver.current_url
        if self.flag_isFirstRun == True:
          result = self.assertEqual(URL, "http://localhost:5000/login")
        print "PASSED",


    # TC1.2 - UserRegister [Invalid registration]
    def test_01_02_Register_Invalid(self):
        print "\n TEST - TC1.2 - UserRegister [Invalid registration]...",
        driver = self.driver
        driver.get("http://localhost:5000/")
        driver.find_element_by_xpath("//div[@onclick='w3_open()']").click()
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("test")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("//div[@onclick='w3_open()']").click()
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("test")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        URL = driver.current_url
        if self.flag_isFirstRun == True:
          result = self.assertEqual(URL, "http://localhost:5000/register")
        print "PASSED",


    #USER LOGIN TEST CASES
    #
    # TC2.1 - UserLogin[Successful login]
    def test_02_01_Login_Success(self):
        print "\n TEST - TC2.1 - UserLogin[Successful login]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        time.sleep(1)
        URL = driver.current_url
        result = self.assertEqual(URL, "http://localhost:5000/")
        print "PASSED",


    # TC2.2 - UserLogin[Failed login - Username]
    def test_02_02_Login_Fail_Username(self):
        print "\n TEST - TC2.2 - UserLogin[Failed login - Username]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("dead@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        time.sleep(1)
        URL = driver.current_url
        result = self.assertEqual(URL, "http://localhost:5000/login")
        print "PASSED",

    # TC2.2 - UserLogin[Failed login - PW]
    def test_02_03_Login_Fail_PW(self):
        print "\n TEST - TC2.3 - UserLogin[Failed login - PW]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test_wrongPW")
        driver.find_element_by_id("submit").click()
        time.sleep(1)
        URL = driver.current_url
        result = self.assertEqual(URL, "http://localhost:5000/login")
        print "PASSED",


    # ADD RECIPE TEST CASES
    #
    # TC3.1 - AddRecipe[Successfully added]
    def test_03_01_AddRecipe_Success(self):
        print "\n TEST - TC3.1 - AddRecipe[Successfully added]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.get("http://localhost:5000/recipe/add")

        #Generate test recipe
        recipeURL = ""
        for i in range(0, 50):
          val = random.randint(1,999999)

          #Try the URL to see if it is valid
          try:
            response = urllib2.urlopen('https://www.allrecipes.com/recipe/' + str(val))
            recipeURL = "https://www.allrecipes.com/recipe/" + str(val)
            break
          except:
            continue

        driver.find_element_by_id("URL").click()
        driver.find_element_by_id("URL").clear()
        driver.find_element_by_id("URL").send_keys(recipeURL)
        driver.find_element_by_id("submit").click()
        time.sleep(5)


        localURL = driver.current_url
        #print URL
        if "http://localhost:5000/recipe/view/?recipe_id" in localURL:
          print "PASSED",


    # TC3.2 - AddRecipe[Failure to add (Duplicate)]
    def test_03_02_AddRecipe_FailureDuplicate(self):
        print "\n TEST - TC3.2 - AddRecipe[Failure to add (Duplicate)]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.get("http://localhost:5000/recipe/add")

        driver.find_element_by_id("URL").click()
        driver.find_element_by_id("URL").clear()
        driver.find_element_by_id("URL").send_keys(recipeURL)
        driver.find_element_by_id("submit").click()
        time.sleep(5)

        URL = driver.current_url
        #print URL
        result = self.assertEqual(URL, "http://localhost:5000/recipe/add")
        print "PASSED",



    # TC3.3 - AddRecipe[Failure to add (Invalid URL)]
    def test_03_03_AddRecipe_FailureInvalidURL(self):
        print "\n TEST - TC3.3 - AddRecipe[Failure to add (Invalid URL)]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.get("http://localhost:5000/recipe/add")

        driver.find_element_by_id("URL").click()
        driver.find_element_by_id("URL").clear()
        driver.find_element_by_id("URL").send_keys("http://www.youtube.com")
        driver.find_element_by_id("submit").click()
        time.sleep(4)

        URL = driver.current_url
        #print URL
        result = self.assertEqual(URL, "http://localhost:5000/recipe/add")
        print "PASSED",







    # EDIT RECIPE TEST CASES
    #
    # TC5.1 - EditRecipe[Name/Description]
    def test_05_01_DeleteRecipe_Success(self):
        print "\n TEST - TC5.1 - EditRecipe[Name/Description]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.get("http://localhost:5000/recipe/view_all")

        driver.find_element_by_name("quantity_id").click()
        driver.find_element_by_id("editable").click()
        driver.find_element_by_name("quantity_id").click()
        driver.find_element_by_xpath("(//input[@id='name'])[2]").click()
        driver.find_element_by_xpath("(//input[@id='name'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[2]").send_keys("TEST")
        driver.find_element_by_id("description").click()
        driver.find_element_by_id("description").clear()
        driver.find_element_by_id("description").send_keys("TEST")
        driver.find_element_by_id("submit").click()

        time.sleep(2)

        URL = driver.current_url
        #print URL
        if "http://localhost:5000/recipe/view/?recipe_id" in URL:
          print "PASSED",








    ##############################################################################
    # ***NEED TO RUN AT END SO WE CAN EDIT FIRST***
    # DELETE RECIPE TEST CASES
    #
    # TC4.1 - DeleteRecipe[Successful]
    def test_98_04_01_DeleteRecipe_Success(self):
        print "\n TEST - TC4.1 - DeleteRecipe[Successful]...",
        driver = self.driver
        driver.get("http://localhost:5000/login")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("test@rpi.edu")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("submit").click()
        driver.get("http://localhost:5000/recipe/view_all")

        driver.find_element_by_name("recipe_id").click()
        time.sleep(2)

        URL = driver.current_url
        #print URL
        result = self.assertEqual(URL, "http://localhost:5000/recipe/view_all")
        print "PASSED",



    ##LEAVE THIS LAST
    #DUMMY TEST to make print statements in terminal display correct
    def test_99_01_dummyTest_page(self):
        self.assertEqual("!", "!")
        print


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    firstRun = raw_input("First run?: (Y/N)")
    if firstRun.lower() != "y":
      flag_isFirstRun = False
    else:
      flag_isFirstRun = True




    unittest.main()

