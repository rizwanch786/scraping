from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

def main_page_data():
    data = []
    pages = np.arange(1, 3, 1)
    for page in pages:
        driver.get(
            f"https://etherscan.io/txs?a=0xC49BE2b36C2e03d9B95f2194a1F28813a7C1Af5C&p={str(page)}"
        )


        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup.title.text)

        table_data = soup.find("table", {"class": "table"})

        table_body = table_data.find('tbody')
        rows = table_body.find_all('tr')

        columns = [i.get_text(strip=True) for i in table_data.find_all("th")]
        columns.append('Transaction Fee')
        columns.insert(4,'Time Zone')

        data.extend(
            [td.get_text(strip=True) for td in tr.find_all("td")]
            for tr in table_data.find("tbody").find_all("tr")
        )

        df = pd.DataFrame(data,columns=columns)
        df.to_excel("data.xlsx", index=False)



def internal_data():
    gass_price = None
    ether_price = None
    transaction_fee = None
    button_price = None
    transaction_details = []
    df = pd.read_excel('data copy.xlsx')
    links = df.iloc[:,1]
    # print(links)
    for txn in links:
        driver.get(f"https://etherscan.io/tx/{str(txn)}")
        time.sleep(2)
        soup1 = BeautifulSoup(driver.page_source, 'html.parser')

        # Transaction Fee
        transaction_fee = soup1.find('span', {'id': 'ContentPlaceHolder1_spanTxFee'}).text

        # Ether Price
        ether_price = soup1.find('span', {"id": "ContentPlaceHolder1_spanClosingPrice"}).text
        ether_price = ether_price.replace('/', "")
        ether_price = ether_price.replace("\n", "")

        # Gass Price
        gass_price = soup1.find('span', {"id": "ContentPlaceHolder1_spanGasPrice"}).text
        gass_price = gass_price.replace("\n", "")
        # button data
        button_price = soup1.find('button', {'id' : 'txfeebutton'}).text
        # try:
        #     button_filter = driver.find_element(By.ID,'txfeebutton')
        #     button_filter.click()
        #     time.sleep(1)
        #     button_price = soup1.find('button', {'id' : 'txfeebutton'}).text
        # except:
        #     continue

        transaction_details.append([transaction_fee, button_price, gass_price, ether_price])

    df1 = pd.DataFrame(transaction_details,columns=['Transaction Fee', 'Button Price', 'Gass Price', 'Ether Price'])
    df['Transaction Fee'] = df1.iloc[:,0]
    df['Button Price'] = df1.iloc[:,1]
    df['Gass Price'] = df1.iloc[:,2]
    df['Ether Price'] = df1.iloc[:,3]
    df.to_csv('data.xlsx')

internal_data()
driver.close()