# Conditional Commads:
# is_displayed(), is_enabled(), is_selected()


from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.google.com/')
search_bar = driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# return True or False Based on Element Status
print(search_bar.is_displayed())
# return True or False Based on Element Status
print(search_bar.is_enabled())
print(search_bar.is_selected())

# is_enabled()
# driver.get('https://getbootstrap.com/docs/5.0/forms/checks-radios/')
# radio_button = driver.find_element(by = By.ID, value='flexCheckDefault')
# time.sleep(2)
# print(radio_button.is_enabled())
# radio_button = driver.find_element(by = By.ID, value='flexRadioDisabled')
# time.sleep(5)
# print(radio_button.is_displayed())
# print(radio_button.is_selected())
driver.quit()
