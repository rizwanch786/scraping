from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.zameen.com/Homes/Lahore-1-1.html")
while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # time.sleep(2)  
    try:
        driver.find_element(By.CLASS_NAME ,'d02376f9 ').click()
        print('click')
    except:
        break
