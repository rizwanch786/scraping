from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
# print(driver.page_source)

# search something from google
search_bar = driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys('Python')
driver.find_element(
    by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
# driver.close() # Close currently focused browser

driver.quit()  # Close all the browsers
