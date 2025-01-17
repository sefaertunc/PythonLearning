from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
import os

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