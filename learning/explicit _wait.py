# By using the Explicit Wait command, the WebDriver is directed to wait until a certain condition occurs before proceeding with executing the code. Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load.
# Documentation: An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. There are some convenience methods provided that help you write code that will wait only as long as required. WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Firefox()
driver.get('https://www.google.com/')

search_bar = driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys('Python')
# Explicit Wait
wait = WebDriverWait(driver, 10)
element = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')))
element.click()
time.sleep(5)

driver.quit()
