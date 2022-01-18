from lib2to3.pgen2 import driver
from random import random
from selenium import webdriver
import time 
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PostTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_post_valid(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://phongtro123.com/dang-nhap-tai-khoan")
        driver.find_element_by_id("inputPhoneEmailLogin").send_keys("0983058005") 
        driver.find_element_by_id("password").send_keys("Abc123!@#")    
        driver.find_element_by_class_name("btn-submit").submit()   

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("Phongtro123.com - Kênh thông tin Phòng Trọ số 1 Việt Nam"))

        driver.get("https://phongtro123.com/quan-ly/dang-tin-moi.html")
        url = "https://phongtro123.com/quan-ly/dang-tin-moi.html"

        # Choose province 
        driver.find_element_by_id("select2-province_id-container").click()
        type_input_select = '//li[contains(text(),"Đà Nẵng")]'
        driver.find_element_by_xpath(type_input_select).click()

        time.sleep(3)

        # Choose district 
        driver.find_element_by_id("select2-district_id-container").click()
        type_input_select_district = '//li[contains(text(),"Quận Hải Châu")]'
        driver.find_element_by_xpath(type_input_select_district).click()

        time.sleep(4)

        # Choose phuongxa
        driver.find_element_by_id("select2-phuongxa-container").click()
        type_input_select_px = '//li[contains(text(),"Phường Hòa Cường Nam")]'
        driver.find_element_by_xpath(type_input_select_px).click()

        time.sleep(3)

        # Choose duong
        driver.find_element_by_id("select2-duong-container").click()
        type_input_select_duong = '//li[contains(text(),"Núi Thành")]'
        driver.find_element_by_xpath(type_input_select_duong).click()

        time.sleep(3)

        driver.find_element_by_id("street_number").send_keys("33 Xo Viet") 

        # Choose danhmuc
        driver.find_element_by_id("post_cat").send_keys("Phòng trọ, nhà trọ")   


        rd = random()

        driver.find_element_by_id("post_title").send_keys("tim ban o ghep than thien nhieu tien " + str(rd))

        driver.find_element_by_id("post_content").send_keys("mo ta...")

        driver.find_element_by_id("giachothue").send_keys("2500000")

        driver.find_element_by_id("post_content-error").text


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

