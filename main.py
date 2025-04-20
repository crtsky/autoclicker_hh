from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import os

chrome_options = Options()
chrome_options.add_argument("--window-size=1280,720")

page_source = "https://ryazan.hh.ru/account/login"
user = os.getenv('HH_USERNAME')
passwrd = os.getenv('HH_PASSWRD')

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(page_source)
    
    time.sleep(5)
    
    login_element = driver.find_element(By.CSS_SELECTOR, "button[data-qa='submit-button']")
    login_element.click()

    cred_type_email = driver.find_element(By.XPATH, "//input[@data-qa='credential-type-EMAIL']")
    cred_type_email_action = cred_type_email.find_element(By.XPATH, "..")
    cred_type_email_action.click()

    login_name_element = driver.find_element(By.CSS_SELECTOR, "input[data-qa='applicant-login-input-email']")
    login_name_element.send_keys(user)

    time.sleep(1)

    login_element = driver.find_element(By.CSS_SELECTOR, "button[data-qa='expand-login-by-password']")
    login_element.click()
    time.sleep(1)
    
    login_pass_element = driver.find_element(By.CSS_SELECTOR, "input[data-qa='applicant-login-input-password']")
    login_pass_element.send_keys(passwrd)
    time.sleep(1)

    login_action_element = driver.find_element(By.CSS_SELECTOR, "button[data-qa='submit-button']")
    login_action_element.click()
    time.sleep(5)
    
    resumes_page_element = driver.find_element(By.CSS_SELECTOR, "div[data-qa='mainmenu_myResumes']")
    resumes_page_element.click()

    time.sleep(5)

    refresh_element = driver.find_element(By.XPATH, "//button[@data-qa='resume-update-button resume-update-button_actions']")
    driver.execute_script("arguments[0].scrollIntoView();", refresh_element)
    refresh_element.click()
    
    time.sleep(5)

finally:
    driver.quit()
    print("succes")