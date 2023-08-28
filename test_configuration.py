from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get(
    f"https://etherscan.io/txs?a=0xC49BE2b36C2e03d9B95f2194a1F28813a7C1Af5C&p={str(page)}"
)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.title.text)

driver.close()