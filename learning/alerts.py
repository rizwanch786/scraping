# # Working with alerts
# Alert(driver).accept()
# Alert(driver).dismiss()
# Alert Methods
# The major methods during handling of alerts in Selenium include –

# accept() – Accepts the alert available.
# dismiss() – Dismisses the alert available.
# send_keys(keysToSend) – Send Keys to the Alert.
# text – Gets the text of the Alert.

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)
driver.find_element(
    by=By.XPATH, value='//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)
# # Click on Ok button
# Alert(driver).accept()

# Click on Cancel button
Alert(driver).dismiss()
# Gets the text of the Alert
alert = Alert(driver)
alert_text = alert.text
print(alert_text)
# not working old vision
driver.switch_to_alert().accept()
time.sleep(2)
driver.quit()
