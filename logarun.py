# HTML/XML encoding for the calendar url

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import html
import http.server

driver = webdriver.Edge()

class LogarunCredentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class StravaCredentials:
    def __init__(self, client_id, client_secret, port):
        self.client_id = client_id
        self.client_secret = client_secret
        self.port = port
        self.scope = 'activity:read_all'
        self.redirect_URI = f'http://localhost:{port}'


def main():
    login()
    edit_url = 'http://www.logarun.com/Edit.aspx?username=william.tucker&date=12/08/2022'


"""
Redirect the user to authentication url. Need to set the scope to everything. 
User is redirected to localhost after accepting the authorization.
Handle request to extract authorization code and scope
Make a POST to receive access_token and refresh_tokens
"""
# handler function


def authenticate():
    strava_creds = StravaCredentials('98562', '1529ac60728f98d6ac564ff4e18e03687eed5356', 5000)
    server = http.server.HTTPServer(('', strava_creds.port), handler)

    URL = ("https://www.strava.com/oauth/authorize?client_id={0}&"
            "redirect_uri={1}&"
            "approval_prompt=auto&"
            "response_type=code&"
            "scope={2}").format(strava_creds.client_id, strava_creds.redirect_URI, strava_creds.scope)

    print(URL)



# log into logarun
def login():
    global driver

    # Logarun credentials
    creds = LogarunCredentials('william.tucker', 'chesterr1')
    
    # Enter credentials into login page
    driver.get('http://www.logarun.com/logon.aspx')
    username_element = driver.find_element(By.ID, 'LoginName')
    password_element = driver.find_element(By.ID, 'Password')
    username_element.send_keys(creds.username)
    password_element.send_keys(creds.password)
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