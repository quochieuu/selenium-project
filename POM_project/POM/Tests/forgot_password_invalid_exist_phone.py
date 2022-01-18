from lib2to3.pgen2 import driver
from selenium import webdriver
import time 
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ForgotPasswordTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_forgot_invalid(self):
        driver = self.driver
        driver.get("https://phongtro123.com/quen-mat-khau")
        driver.find_element_by_id("inputPhoneEmailForgot").send_keys("0983058001")    
        driver.find_element_by_class_name("js-forgot-password-next-step").submit()    

        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

