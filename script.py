from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

###############################
load_dotenv()
website_link = "http://phc.prontonetworks.com/cgi-bin/authlogin"
username = os.getenv('USERID')
password = os.getenv('PASS')

###############################

element_for_username = 'userId'
element_for_password = 'password'
element_for_submit = 'Submit22'

###############################

# for Chrome and Brave
browser = webdriver.Chrome()

# For Firefox
#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#for macOS users ( Safari )
#browser = webdriver.Safari()	

browser.get((website_link))

try:
	username_element = browser.find_element(by=By.NAME, value=element_for_username)
	username_element.send_keys(username)		
	password_element = browser.find_element(by=By.NAME, value=element_for_password)
	password_element.send_keys(password)
	signInButton = browser.find_element(by=By.NAME, value=element_for_submit)
	signInButton.click()
	
	#### to quit the browser ####
	time.sleep(3)
	browser.quit()
    #### to kill the browser process ####
    # time.sleep(1)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print("Some error occured :(")

	#### to quit the browser uncomment the following lines ####
	# browser.quit()
    #### to kill the browser process ####
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)