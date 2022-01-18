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

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://phongtro123.com/dang-nhap-tai-khoan")
        
        driver.find_element_by_id("inputPhoneEmailLogin").send_keys("0983058005") 
        driver.find_element_by_id("password").send_keys("Abc123!@#")    
        driver.find_element_by_class_name("btn-submit").submit()   

        login_success_url = "https://phongtro123.com/"
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("Phongtro123.com - Kênh thông tin Phòng Trọ số 1 Việt Nam"))

        if self.driver.current_url == login_success_url:
            print("PASS")
        else:
            print("FAIL")

        time.sleep(10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

