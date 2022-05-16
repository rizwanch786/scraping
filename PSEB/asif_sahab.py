from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("https://pseb.org.pk/app/company_directory.php")
driver.maximize_window()
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.title.text)

time.sleep(5)
# button_filter = driver.find_element(By.ID, "filterbtn")
# button_filter.click()
# # driver.execute_script("arguments[0].click();", button_filter);
# # time.sleep(10)
# print(soup.title.text)


table_data = soup.find("table", {"class": "dataTable"})
columns = [i.get_text(strip=True) for i in table_data.find_all("th")]
print(columns)
data = []
links = []
for tr in table_data.find("tbody").find_all("tr"):
        data.append([td.get_text(strip=True) for td in tr.find_all("td")])
        links.append([f"https://pseb.org.pk/app/{a['href']}" for a in tr.find_all('a', href=True)])

# print(data)
# print(len(data))


print(links)
print(len(links))

df = pd.DataFrame(data,columns=columns)
df.to_excel("Asif.xlsx", index=False)
linked_data = []

for i in range(len(links)):
        driver.get(links[i][0])
        soup_next = BeautifulSoup(driver.page_source, 'html.parser')
#     print(soup_next.title.text)
        link_table_data = soup_next.find("table", {"class": "table table-striped"})
        # link_columns = [i.get_text(strip=True) for i in link_table_data.find_all("th")]
        temp = []
        for tr in link_table_data.find("tbody").find_all("tr"):
                        # linked_data.append([td.get_text(strip=True) for td in tr.find("td")])
                temp.extend(td.get_text(strip=True) for td in tr.find_all("td"))
        linked_data.append(temp)


# print(link_columns)
print(linked_data)
print(len(linked_data))
df1 = pd.DataFrame(linked_data,columns=['Address', 'City', 'Phone', 'Email', 'Contact Person', 'Designation','Contacts', 'URL'])
df1.to_excel("links.xlsx", index=False)
driver.close()
