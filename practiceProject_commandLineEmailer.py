# Program that takes an email address and string of text on the command line and then
# using selenium, logs in to your email account and send an email of the string to the provided address.

import sys, time
from selenium import webdriver

# Opening gmail
browser = webdriver.Chrome()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
# Login / Password
email = browser.find_element_by_id('identifierId')
email.send_keys('your_email')
nextBtn = browser.find_element_by_class_name('VfPpkd-RLmnJb')
nextBtn.click()
time.sleep(5)
password = browser.find_element_by_id('password')
password.send_keys('your_password')
password.submit()