import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(ChromeDriverManager().install())

#test register success with valid account
def test_login_success_with_valid_account():
    driver.get("https://phongtro123.com/dang-nhap-tai-khoan")
    driver.find_element_by_id("inputPhoneEmailLogin").send_keys("0983058005") 
    driver.find_element_by_id("password").send_keys("Abc123!@#")    
    driver.find_element_by_class_name("btn-submit").submit()   

    login_success_url = "https://phongtro123.com/"
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Phongtro123.com - Kênh thông tin Phòng Trọ số 1 Việt Nam"))

    if driver.current_url == login_success_url:
        print("PASS")
    else:
        print("FAIL")

    time.sleep(10)
    driver.quit()

test_login_success_with_valid_account()