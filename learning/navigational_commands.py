# navigation: click on next or back page of browser buttons
# back(), forward(), refresh()
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get('https://www.google.com/')
search_bar = driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys('selenium')
driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

time.sleep(2)
driver.find_element(
    by=By.LINK_TEXT, value='Documentation').click()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.quit()
