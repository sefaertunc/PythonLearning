import time
from logging import raiseExceptions

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.speedtest.net/de")

time.sleep(7)
start_button = driver.find_element(By.CSS_SELECTOR,".js-start-test.test-mode-multi")
start_button.click()

time.sleep(40)

down_speed = driver.find_element(By.CSS_SELECTOR,".result-data-large.number.result-data-value.download-speed")
up_speed = driver.find_element(By.CSS_SELECTOR,".result-data-large.number.result-data-value.upload-speed")
print(f"Download Speed: {down_speed.text}\nUpload Speed: {up_speed.text}")

