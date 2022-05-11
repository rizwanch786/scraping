from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

def get_main_page_links():
    driver.get("https://www.odoo.com/customers")
    links = []

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # time.sleep(2)
        main_div = soup.find_all('div', {'class': 'media mt-3'})
        for a in main_div:
            for link in a.find_all('a', {'class': 'd-block mr-3 text-center o_width_128'}, href = True):
                print(f"https://www.odoo.com//{link['href']}")
                links.append(f"https://www.odoo.com//{link['href']}")
        
        print(links)
        print(len(links))
        try:
            driver.find_element_by_partial_link_text('Next').click()
        except:
            break
    df = pd.DataFrame(links,columns=['links'])
    df.to_csv('odoo_customers_links.xlsx')
    
def get_data():    
    df = pd.read_excel('customers_links.xlsx')
    links = df.iloc[:,-1]
    links = list(links)
    details = []
    for i in range(10000, len(links)):
        driver.get(links[i])
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        try:
            partner_name = soup.find('h1', {'id': 'partner_name'}).text
            partner_name = partner_name.replace('\n', ' ')
        except:
            partner_name = "Null"
        try:
            implemented_by = soup.find('div', {'class': 'card-body text-center'}).find('h4').text
            implemented_by = implemented_by.replace("\n", " ")
        except:
            implemented_by = "Null"
        try:        
            address = soup.find('span', {'class': 'w-100 o_force_ltr d-block'}).text
        except:
            address = "Null"
        try:        
            phone_no = soup.find('span', {'itemprop': 'telephone'}).text
        except:
            phone_no = "Null"
        try:        
            email_add = soup.find('span', {'itemprop':'email'}).text
        except:
            email_add = "Null"
        print(links[i])
        print(i+1)
        print(email_add)
        print(phone_no)
        details.append([links[i],partner_name, implemented_by, address, phone_no, email_add])
        df = pd.DataFrame(details,columns=['URL', 'Partner ID', 'Implemented By', 'Address', 'Phone No', 'Email'])
        df.to_csv('odoo_customer_10k_end_final.xlsx')
            
get_data()
# get_main_page_links()
driver.quit()

