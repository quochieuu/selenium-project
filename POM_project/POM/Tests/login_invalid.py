from lib2to3.pgen2 import driver
from selenium import webdriver
import time 
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_invalid(self):
        driver = self.driver
        driver.get("https://phongtro123.com/dang-nhap-tai-khoan")
        
        driver.find_element_by_id("inputPhoneEmailLogin").send_keys("0983058004") 
        driver.find_element_by_id("password").send_keys("Abc123!@#$---")    
        driver.find_element_by_class_name("btn-submit").submit()   

        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

