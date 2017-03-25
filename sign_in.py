import read
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

NAME, EMAIL, PASS = range(3)

driver = webdriver.Chrome()

accounts = read.read_accounts()
current_account = accounts[10]

driver.get('https://www.kickstarter.com/login?ref=nav')
driver.find_element_by_id('user_session_email').send_keys(current_account[EMAIL])
driver.find_element_by_id('user_session_password').send_keys(current_account[PASS])
driver.find_element_by_name('commit').click()

while True:
    if input('exit? y/n\n') == "y":
        break

driver.quit()
