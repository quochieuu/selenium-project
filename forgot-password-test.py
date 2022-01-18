import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

def verify_can_not_forgot_password_with_not_exist_phone_number():
    driver.get("https://phongtro123.com/quen-mat-khau")
    driver.find_element_by_id("inputPhoneEmailForgot").send_keys("0983058001")    
    driver.find_element_by_class_name("js-forgot-password-next-step").submit()   

    if driver.current_url == driver.current_url:
        print("PASS")
    else:
        print("FAIL")

    time.sleep(5)
    driver.quit()


def verify_can_not_forgot_password_with_invalid_phone_number():
    driver.get("https://phongtro123.com/quen-mat-khau")
    driver.find_element_by_id("inputPhoneEmailForgot").send_keys("098305800123123!@")    
    driver.find_element_by_class_name("js-forgot-password-next-step").submit()   

    if driver.current_url == driver.current_url:
        print("PASS")
    else:
        print("FAIL")

    time.sleep(5)
    driver.quit()


# verify_can_not_forgot_password_with_not_exist_phone_number()
# verify_can_not_forgot_password_with_invalid_phone_number()