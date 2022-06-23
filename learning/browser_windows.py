# window_handles
# current_window_handle
# switch_to_window
# maximize_window
# minimize_window
from logging import handlers
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Firefox()
driver.get('https://www.hyrtutorials.com/p/window-handles-practice.html')
time.sleep(2)
driver.find_element(by=By.ID, value='newTabBtn').click()
# driver.save_screenshot('/home/rizwan/Documents/Scraping/learning/browsers.png')
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)
print(driver.window_handles)
handles = driver.window_handles
for h in handles:
    # Chromedriver has been updated from version 95.0.4638.17 to ChromeDriver 96.0.4664.45
    # driver.switch_to.default_content()
    time.sleep(2)
    # switch_to_window not working 
    driver.switch_to.window(h)
    print(driver.title)
    time.sleep(5)

driver.quit()
