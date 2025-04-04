from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os

page_source = "https://ryazan.hh.ru/account/login"
user = os.getenv('HH_USERNAME')
passwrd = os.getenv('HH_PASSWRD')

driver = webdriver.Firefox()

try:
    driver.get(page_source)
    
    time.sleep(5)
    
    login_expand_element = driver.find_element(By.LINK_TEXT, "Войти с паролем")
    login_expand_element.click()
    
    login_name_element = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-username']")
    login_pass_element = driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-input-password']")
    login_action_element = driver.find_element(By.CSS_SELECTOR, "button[data-qa='account-login-submit']")
    
    login_name_element.send_keys(user)
    login_pass_element.send_keys(passwrd)
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