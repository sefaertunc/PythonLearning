from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import os

load_dotenv("../.venv/.env")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://tiss.tuwien.ac.at/curriculum/studyCodes.xhtml?dswid=7182&dsrid=857")
driver.maximize_window()
time.sleep(2)

lang_eng = driver.find_element(By.NAME, "language_en")
lang_eng.click()
time.sleep(2)

all_programs_list = driver.find_elements(By.CSS_SELECTOR, ".studyCodeNameColumn")
time.sleep(2)

masters_dic = {element.text:element.find_element(By.CSS_SELECTOR, "a") for element in all_programs_list if element.text.split()[0].lower() == 'master'}
time.sleep(2)


