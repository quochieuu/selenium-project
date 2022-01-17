import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import random


driver = webdriver.Chrome(ChromeDriverManager().install())

def test_create_new_post_successful():
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

    time.sleep(3)

    driver.find_element_by_id("post_title").send_keys("Tim ban o ghep tai duong nui thanh" + str(random()))

    driver.find_element_by_id("post_content").send_keys("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

    driver.find_element_by_id("giachothue").send_keys("2500000")

    driver.find_element_by_id("post_acreage").send_keys("50")

    driver.find_element_by_class_name("js-btn-hoan-tat").submit()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Đăng lại tin - Phongtro123.com"))

    if driver.current_url != url:
        print("PASS")
    else:
        print("FAIL")

    time.sleep(10)
    driver.quit()


test_create_new_post_successful()
# test_create_new_post_fail_with_short_title()