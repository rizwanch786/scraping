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
data = []
links = []
i  = 10
while i > 0:
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(10)

    # print('Heloooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
    table_data = soup.find("table", {"class": "dataTable"})
    columns = [i.get_text(strip=True) for i in table_data.find_all("th")]
    print(columns)

    for tr in table_data.find("tbody").find_all("tr"):
        data.append([td.get_text(strip=True) for td in tr.find_all("td")])
        links.extend(
            f"https://pseb.org.pk/app/{a['href']}"
            for a in tr.find_all('a', href=True)
        )

    print(data)
    print(len(data))
    i -= 1
    try:
        driver.find_element(By.ID, "myTable_next").click()
        # driver.find_element_by_partial_link_text('Next').click()
    except:
        break
print(len(data))
df = pd.DataFrame(data,columns=columns)
df.insert(0, "Company Details URL", links)
df.to_excel("total_records.xlsx", index=False)

print(links)
print(len(links))

# get next data
linked_data = []

for i in range(len(links)):
    driver.get(links[i])
    # time.sleep(2)
    soup_next = BeautifulSoup(driver.page_source, 'html.parser')
    # time.sleep(2)
    link_table_data = soup_next.find("table", {"class": "table table-striped"})
    temp = []
    for tr in link_table_data.find("tbody").find_all("tr"):
        temp.extend(td.get_text(strip=True) for td in tr.find_all("td"))
    linked_data.append(temp)


# print(linked_data)
print(len(linked_data))

df1 = pd.DataFrame(linked_data,columns=['Address', 'City', 'Phone', 'Email', 'Contact Person', 'Designation','Contacts', 'URL'])
# df1['Organization Name'] = df.iloc[:,1]
df1.insert(0, "Organization Name", df.iloc[:,1])
df1.to_excel("inner_data.xlsx", index=False)
driver.quit()