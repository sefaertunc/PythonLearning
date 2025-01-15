from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Sefa")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Ertunc")
email = driver.find_element(By.NAME, "email")
email.send_keys("sefaertnc@gmail.com")
button = driver.find_element(By.CLASS_NAME, "btn-block")
button.click()