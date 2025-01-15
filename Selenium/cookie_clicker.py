from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

def getStoreItems():
    store_elements = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    store_elements.pop(len(store_elements) - 1)
    return store_elements

def getMoney():
    money = driver.find_element(By.ID, "money").text
    return int(money.replace(",", ""))

def checkBuyingOptions():
    while True:
        store_elements = getStoreItems()
        purchase_made = False

        for element_index in range(len(store_elements) - 1, -1, -1):
            try:
                item_text = store_elements[element_index].text
                if "-" in item_text:
                    price = int(item_text.split("-")[1].strip().replace(",", ""))
                    my_money = getMoney()
                    if my_money >= price:
                        store_elements[element_index].click()
                        purchase_made = True
                        break
            except Exception as e:
                print(f"Error during purchase: {e}")

        if not purchase_made:
            break

timeout = time.time() + 5

while True:
    cookie.click()

    if time.time() > timeout:
        checkBuyingOptions()
        timeout = time.time() + 5
