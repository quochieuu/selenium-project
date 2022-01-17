from email import message
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#test register success with valid account
def test_register_success_with_valid_account():
    driver.get("https://phongtro123.com/dang-ky-tai-khoan")
    driver.find_element_by_id("inputFullName").send_keys("Hieu Ho")   
    driver.find_element_by_id("inputPhone").send_keys("0983058005") 
    driver.find_element_by_id("password").send_keys("Abc123!@#")    
    driver.find_element_by_class_name("btn-submit").submit()   

    register_success_url = "https://phongtro123.com/xac-thuc-tai-khoan"
    if driver.current_url == register_success_url:
        print("PASS")
    else:
        print("FAIL")

    driver.quit()


#test can not register with invalid phone
def test_register_fail_with_invalid_phone_number():
    url = "https://phongtro123.com/dang-ky-tai-khoan"
    driver.get(url)
    get_url = driver.current_url
    
    driver.find_element_by_id("inputFullName").send_keys("Hieu Ho")   
    driver.find_element_by_id("inputPhone").send_keys("0983058005123123") 
    driver.find_element_by_id("password").send_keys("Abc123!@#")    
    driver.find_element_by_class_name("btn-submit").submit()   

    register_success_url = "https://phongtro123.com/xac-thuc-tai-khoan"
    print(url)
    print(get_url)
    if get_url == url:
        print("PASS")
    elif get_url == register_success_url:
        print("FAIL")
    else:
        print("FAIL")

    driver.quit()

def test_register_fail_with_invalid_password():
    url = "https://phongtro123.com/dang-ky-tai-khoan"
    driver.get(url)
    get_url = driver.current_url
    
    driver.find_element_by_id("inputFullName").send_keys("Hieu Ho")   
    driver.find_element_by_id("inputPhone").send_keys("0983058005") 
    driver.find_element_by_id("password").send_keys("1")    
    driver.find_element_by_class_name("btn-submit").submit()   

    register_success_url = "https://phongtro123.com/xac-thuc-tai-khoan"
    print(url)
    print(get_url)
    if get_url == url:
        print("PASS")
    elif get_url == register_success_url:
        print("FAIL")
    else:
        print("FAIL")

    driver.quit()


# test_register_success_with_valid_account()
# test_register_fail_with_invalid_phone_number()
# test_register_fail_with_invalid_password()