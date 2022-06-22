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
# # print number of links available on current page
# page_links = driver.find_elements(by=By.TAG_NAME, value='a')
# print(len(page_links))
# for link in page_links:
#     print(link.text)
if driver.find_element(by=By.LINK_TEXT, value='Documentation').is_displayed():
    driver.find_element(by=By.LINK_TEXT, value='Documentation').click()
else:
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Doc').click()

time.sleep(2)
driver.quit()
