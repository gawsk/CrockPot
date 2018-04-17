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

flag_isFirstRun = False

class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.flag_isFirstRun = flag_isFirstRun
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # Must start with 'test_'
    def test_01_Register(self):
        print "\n TEST - Load Register Page...",
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

    def test_02_Login_Success(self):
        print "\n TEST - Login Page...",
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

    def test_03_Login_Fail_Username(self):
        print "\n TEST - Login Fail - Bad Username...",
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

    def test_04_Login_Fail_PW(self):
        print "\n TEST - Login Fail - Bad Password...",
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


    def test_05_AddRecipe_Success(self):
        print "\n TEST - Add Recipe...",
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
        driver.find_element_by_id("URL").send_keys("https://www.allrecipes.com/recipe/15965/lemon-icebox-pie-iii/?internalSource=previously%20viewed&referringContentType=home%20page&clickId=cardslot%202")
        driver.find_element_by_id("submit").click()
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

