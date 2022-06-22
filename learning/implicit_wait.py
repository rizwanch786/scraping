# Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception. Once this time is set, WebDriver will wait for the element before the exception occurs. Once the command is in place, Implicit Wait stays in place for the entire duration for which the browser is open.
# Documentation: An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.google.com/')
# Seconds
driver.implicitly_wait(10)
# assert "Welcome: " in driver.title

search_bar = driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys('Python')
driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
driver.quit()
