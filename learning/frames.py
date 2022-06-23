# switch_to

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get('https://www.hyrtutorials.com/p/frames-practice.html')
# --------------- frame 1 -------------------------------------
driver.switch_to.frame('frm1')
print('frame 1')
time.sleep(2)
l1 = driver.find_element(by=By.ID, value='selectnav1')
l1 = Select(l1)

print(len(l1.options))
all_options = l1.options
for op in all_options:
    print(op.text)

# set default driver
driver.switch_to.default_content()
# --------------- frame 2 -------------------------------------
driver.switch_to.frame('frm2')
print('frame 2')
time.sleep(2)
l2 = driver.find_element(by=By.ID, value='selectnav1')
l2 = Select(l2)

print(len(l2.options))
all_options = l2.options
for op in all_options:
    print(op.text)
driver.quit()
