from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException 

driver = webdriver.Edge()

def main():
    login()

# log into logarun
def login():
    global driver

    # Logarun credentials
    logarun_username = 'william.tucker'
    logarun_password = 'chesterr1'
    
    # Enter credentials into login page
    driver.get('http://www.logarun.com/logon.aspx')
    username_element = driver.find_element(By.ID, 'LoginName')
    password_element = driver.find_element(By.ID, 'Password')
    username_element.send_keys(logarun_username)
    password_element.send_keys(logarun_password)
    navigate_menu('LoginNow')

def navigate_menu(id):
    global driver
    try:
        element = driver.find_element(By.ID, id)
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
    except StaleElementReferenceException:
        element = driver.find_element(By.ID, id)
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

main()