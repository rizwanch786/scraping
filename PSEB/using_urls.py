from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome()
# driver.maximize_window()
df = pd.read_excel('company_details_links_final.xlsx')
links = df.iloc[:,-1]
linked_data = []
company = []
# for i in range(1500, len(links)):
for i in range(1850, 1900):
    print(links[i])
    driver.get(links[i])
    soup_next = BeautifulSoup(driver.page_source, 'html.parser')
    cam = soup_next.find("div", {"class": "panel-heading"})
    company.append(cam.text)
    link_table_data = soup_next.find("table", {"class": "table table-striped"})
    table_body = link_table_data.find('tbody')
    table_row = table_body.find_all('tr')
    temp = []
    for tr in table_row:
        temp.extend(td.get_text(strip=True) for td in tr.find_all("td"))
    linked_data.append(temp)


print(linked_data)
print(len(linked_data))
df1 = pd.DataFrame(linked_data,columns=['Address', 'City', 'Phone', 'Email', 'Contact Person', 'Designation','Contacts', 'URL'])
df1.insert(0, 'Company Name', company)
df1.to_excel("data1850_1900.xlsx", index=False)
driver.quit()
