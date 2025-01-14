from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

streak = driver.find_elements(By.CSS_SELECTOR, '.small-widget a')
for element in streak:
    print(element.text)

driver.quit()