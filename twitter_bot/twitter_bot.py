import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv("../.venv/.env")

my_pass = os.getenv("PASSWORD")
print(my_pass)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://x.com/home")
driver.maximize_window()

time.sleep(3)

refuse_cookies = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]')
refuse_cookies.click()

time.sleep(3)

sign_in_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a')
sign_in_button.click()

time.sleep(3)

username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
username.send_keys("learningjunky24")

time.sleep(3)

username_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
username_button.click()

time.sleep(3)

password = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys(my_pass)

time.sleep(3)

sign_in = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
sign_in.click()

time.sleep(8)

twit_entry = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
twit_entry.send_keys("Sample Sentence is being written..")
twit_entry_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
twit_entry_button.click()