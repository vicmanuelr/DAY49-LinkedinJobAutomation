from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

driver = webdriver.Firefox()
driver.get(url='https://www.linkedin.com/jobs/search/?currentJobId=3369880868&f_JT=F&geoId=100877388&keywords=Desarrollador%20de%20Python&location=Guatemala&refresh=true')

session_login = driver.find_element(By.CSS_SELECTOR, ".cta-modal__primary-btn")
time.sleep(5)
session_login.click()
time.sleep(5)
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys(USERNAME)

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(PASSWORD)

login_button = driver.find_element(By.CSS_SELECTOR, '.btn__primary--large')
login_button.click()

driver.close()
