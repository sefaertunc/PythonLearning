from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os
import time

load_dotenv("../.venv/.env")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
linkedin_url = "https://www.linkedin.com/feed/"
driver.get(linkedin_url)

username_blank = driver.find_element(By.NAME, "session_key")
password_blank = driver.find_element(By.NAME, "session_password")
sign_in_button = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")

username_blank.send_keys("sefaertnc@gmail.com")
password_blank.send_keys(os.getenv("EMAIL_PASS"))
sign_in_button.click()

jobs_button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a'))
)
jobs_button.click()

time.sleep(5)
job_input = driver.find_element(By.CSS_SELECTOR, '.jobs-search-box__text-input.jobs-search-box__keyboard-text-input.jobs-search-global-typeahead__input')
job_input.send_keys("Security Analyst")

area_input = driver.find_element(By.CSS_SELECTOR, '.jobs-search-box__text-input')
area_input.send_keys("European Union")

area_input.send_keys(Keys.ENTER)

