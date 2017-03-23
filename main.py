# NOTE: must run " pip install -U selenium "

import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

def new_tab(site):
    driver.execute_script('window.open("' + site + '","_blank");')

def change_focus(window):
    driver.switch_to_window(driver.window_handles[sites_open.index(window)])

driver.get('https://www.kickstarter.com/signup?ref=nav')
new_tab('https://lastpass.com/generatepassword.php')
new_tab('http://www.pseudorandom.name/')
new_tab('https://www.guerrillamail.com/inbox')

sites_open = ['KICKSTARTER', 'MAIL', 'RANDOM_NAME', 'RANDOM_PASS']
# I do not know why I have to open up the new tabs opposite from how the indices are laid out in this list

change_focus('RANDOM_PASS')
##driver.get('https://www.google.com')
##driver.find_element_by_name('q').click()
##WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id("selectpw").is_displayed())
#driver.find_element_by_id('selectpw').click()
##WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id("password").is_displayed())                
#driver.find_element_by_id('password').send_keys(Keys.CONTROL, 'c')

password = driver.find_element_by_id('password').get_attribute('value')
change_focus('RANDOM_NAME')
name = driver.find_element_by_tag_name('h1').get_attribute('innerHTML')
change_focus('MAIL')
email = driver.find_element_by_id('email-widget').get_attribute('innerHTML')

print(password)
print(name)
print(email)

change_focus('KICKSTARTER')
driver.find_element_by_id('user_name').send_keys(name)
driver.find_element_by_id('user_email').send_keys(email)
driver.find_element_by_id('user_email_confirmation').send_keys(email)
driver.find_element_by_id('user_password').send_keys(password)
driver.find_element_by_id('user_password_confirmation').send_keys(password)

# click submit button
driver.find_element_by_xpath("//*[@class='btn btn--green btn--block submit']").click()

# write credentials to accounts.txt
with open('accounts.dat', 'rb') as f:
    l = pickle.load(f)

l.append([name, email, password])
print(l)

with open('accounts.dat', 'wb') as f:
    pickle.dump(l, f)

driver.find_element_by_id('js-user_nav_select').click()
driver.find_element_by_link_text('Account').click()
driver.find_element_by_link_text('Re-send verification email').click()

# get the subjects of the emails
change_focus('MAIL')

correct_subject = "Action Needed. Please verify your email address for Kickstarter."
subject_found = False 
while not subject_found:
    subjects = driver.find_elements_by_xpath("//*[@class='td3']")
    for s in subjects:
        if correct_subject in s.get_attribute('innerHTML'):
            email_message = s 
            subject_found = True

email_message.click()

#wait until the message is open
WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id("back_to_inbox_link").is_displayed()) 

links = driver.find_elements_by_tag_name('a')
verification_link = "https://www.kickstarter.com/profile/verify_email?"
for l in links:
    if verification_link in l.get_attribute('innerHTML'):
        l.click()
        driver.switch_to_window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id("js-user_nav_select").is_displayed())
        driver.close()
        break

while True:
    if input('exit? y/n') == "y":
        break

time.sleep(5)
##driver.switch_to_window(driver.window_handles[1])
##
###time.sleep(5) # Let the user actually see something!
##search_box = driver.find_element_by_name('q')
##search_box.send_keys('ChromeDriver')
##search_box.submit()
##time.sleep(5) # Let the user actually see something!
##driver.quit()
driver.quit()

# use the below to delete the latest entry 
##with open('accounts.dat', 'rb') as f:
##    l = pickle.load(f)
##
##l.pop(-1)
##
##with open('accounts.dat', 'wb') as f:
##    pickle.dump(l, f)
