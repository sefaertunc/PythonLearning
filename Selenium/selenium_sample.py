from pandas.io.stata import excessive_string_length_error
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul a')
events_dic = {}
for num in range(len(event_names)):
    events_dic[num] = {'time': event_dates[num].get_attribute('datetime').split('T')[0], 'name':event_names[num].text}

driver.quit()

print(events_dic)