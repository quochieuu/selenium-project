from selenium import webdriver
import time 
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_register_valid(self):
        driver = self.driver

        driver.get("https://phongtro123.com/dang-ky-tai-khoan")
        driver.find_element_by_id("inputFullName").send_keys("Hieu Ho")   
        driver.find_element_by_id("inputPhone").send_keys("0983058005123123") 
        driver.find_element_by_id("password").send_keys("Abc123!@#")    
        driver.find_element_by_class_name("btn-submit").submit()   

        
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

