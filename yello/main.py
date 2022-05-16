from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
import numpy as np

driver = webdriver.Chrome()



def get_main_categories():
    driver.get("https://www.yello.ae/browse-business-directory")
    # time.sleep(5)
    driver.maximize_window()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    section = soup.find('body')
    data = []
    main_category_link = []
    for a in section.find_all('h2'):
        main_category = a.text
        for link in a.find_all('a', href = True):
            print(f"https://www.yello.ae/{link['href']}")
            main_category_link = f"https://www.yello.ae/{link['href']}"
        data.append([main_category, main_category_link]) 
        df = pd.DataFrame(data,columns=['Category','Link'])
        df.to_csv('Categories.xlsx')
    driver.quit()

# get_main_categories()


def get_subCategoryData():
    data = []
    path = r'/home/rizwan/Documents/Scraping/bs4_selenium/yello/Categories.xlsx'
    df = pd.read_csv(path)
    links = df.iloc[:,-1]
    # print(list(links))
    for l in list(links):
        driver.get(l)
        # time.sleep(5)
        driver.maximize_window()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        section = soup.find('body')
        # print(section)
        for a in section.find_all('h2'):
            category = section.find('h1').text
            # print(category)
            sub_category = a.text
            # print(sub_category)
            for link in a.find_all('a', href = True):
                print(f"https://www.yello.ae/{link['href']}")
                sub_category_link = f"https://www.yello.ae/{link['href']}"
                data.append([category, l, sub_category, sub_category_link]) 
                print(data)
                df = pd.DataFrame(data,columns=['Category','Category url','SubCategory','SubCategory url'])
                df.to_csv('SubCategoryData.xlsx')              

# get_subCategoryData()


def getCompaniesData():
    data = []
    path = r'/home/rizwan/Documents/Scraping/bs4_selenium/yello/Property.xlsx'
    df = pd.read_csv(path)
    links = df.iloc[:,-1]
    links = list(links)
    subcategory = df.iloc[:,-2]
    subcategory = list(subcategory)
    Category = df.iloc[:,-4]
    Category = list(Category)
    for l in range(len(links)):
        print(l)
        driver.get(links[l])
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # time.sleep(5)
        # driver.maximize_window()
        pagesNumbers = soup.find('div', {'class': 'pages_container_top'})
        try:
            p_no = pagesNumbers.find('strong').text
            pages = ''.join(p_no[n] for n in range(len(p_no)) if p_no[n] != ',')
            print(int(pages))
            pages = int(pages)
            pg = np.arange(1, (pages/30) + 1, 1)
            for page in pg:
                driver.get(links[l] + '/' + str(page))
                soup1 = BeautifulSoup(driver.page_source, 'html.parser')
                listing = soup1.find('div', {'id':'listings'})
                # print(listing)

                for div in listing.find_all('div', {'class':'company'}):
                    try:
                        for h4 in div.find_all('h4'):
                            company_name = h4.text
                            for link in h4.find_all('a', href = True):
                                print(f"https://www.yello.ae/{link['href']}")
                                data.append([Category[l], subcategory[l], company_name, f"https://www.yello.ae/{link['href']}"])
                                df = pd.DataFrame(data,columns=['Category','SubCategory','Company Name', 'Companies url'])
                                df.to_csv('PropertyCateData.xlsx')
                    except:
                        company_name = 'Null'
        except:
            continue
            
# getCompaniesData()



def getCompaniesDetail():
    data = []
    path = r'/home/rizwan/Documents/Scraping/bs4_selenium/yello/PropertyCateData.xlsx'
    df = pd.read_csv(path)
    companies = df.iloc[:,-1]
    company_name = df.iloc[:,-2]
    company_name = list(company_name)
    subcategory = df.iloc[:,-3]
    subcategory = list(subcategory)
    category = df.iloc[:,-4]
    category = list(category)
    # print(category)
    companies = list(companies)
    for company in range(8157, len(companies)):
        driver.get(companies[company])
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        
        mobile_phone = ''
        fax = ''
        address = ''
        city = ''
        phone_no = ''
        mobile_phone = ''
        fax = ''
        website = ''
        # try:
        #     company_name = soup.find('b',{'id':'company_name'}).text
        #     # print(company_name)
        # except:
        #     company_name = 'Null'
            
        try:
            address = soup.find('div', {'class': 'text location'}).text
            address = address.replace('View Map', '')
            # print(address)
        except:
            address = 'Null'
        
        try:
            city = driver.find_element(By.XPATH, '//*[@id="left"]/div[2]/div/div[4]/div[2]/a[1]')
            city = city.text

        except:
            city = 'Null'
        try:
            phone_no = soup.find('div', {'class':'text phone'}).text
            phone_no = phone_no.replace('\n', ', ')
            # print(phone_no)
        except:
            phone_no = 'Null'
            
        try:
            mobile = driver.find_element(By.XPATH, '//*[@id="left"]/div[2]/div/div[6]/div[2]')
            mobile = mobile.text
            if mobile[-1].isdigit():
                print('mobile phone')
                mobile = mobile.replace('\n', ', ')
                mobile_phone = mobile
        except:
            mobile_phone = 'Null'
        
        try:
            f = driver.find_element(By.XPATH, '//*[@id="left"]/div[2]/div/div[7]/div[2]')
            f = f.text
            if f[-1].isdigit():
                print('fax')
                f = f.replace('\n', ', ')
                fax = f
        except:
            fax = 'Null'
        
        try:
            website = soup.find('div', {'class':'text weblinks'}).text
            # website = website.replace('\n', ' ')
            # print(website)
        except:
            website = 'Null'
        
        data.append([category[company], subcategory[company], company_name[company], companies[company], address, city, phone_no, mobile_phone, fax, website])
        df = pd.DataFrame(data,columns=['Category','SubCategory','Company Name', 'Companies url', 'Address','City', 'Phone No', 'Mobile Phone', 'Fax', 'Website'])
        df.to_csv('PropertyData2.xlsx')

        
#         # try:
#         #     categories = soup.find('div', {'class': 'categories'})
#         #     for a in categories.find_all('a', href = True):
#         #         catgry = a.text
#         #         print(catgry)
#         #         break
#         #     category = category
#         # except:
#         #     category = 'Null'
        
    
getCompaniesDetail()

# # # testing
# # driver = webdriver.Chrome()
# # driver.get('https://www.yello.ae/category/lumber')
# # soup = BeautifulSoup(driver.page_source, 'html.parser')

# # pagesNumbers = soup.find('div', {'class': 'pages_container_top'})
# # # p_no = pagesNumbers.find('strong').text
# # try:
# #     print('continue')
# #     p_no = pagesNumbers.find('strong').text
# #     print('helooooooooooooooooooooo')
# # except:
# #     print('yes')
# # driver.quit()


def getSpecificData():
    data = []
    path = 'https://www.yello.ae/category/property'
    driver.get(path)
        # time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    section = soup.find('body')
    # print(section)
    for a in section.find_all('h2'):
        category = section.find('h1').text
        # print(category)
        sub_category = a.text
        # print(sub_category)
        for link in a.find_all('a', href = True):
            print(f"https://www.yello.ae/{link['href']}")
            sub_category_link = f"https://www.yello.ae/{link['href']}"
            data.append([category, path, sub_category, sub_category_link]) 
            print(data)
            df = pd.DataFrame(data,columns=['Category','Category url','SubCategory','SubCategory url'])
            df.to_csv('Property.xlsx')
# getSpecificData()

# def getSpecificCatData():
#     path = "https://www.yello.ae/category/schools"
#     driver.get(path)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     # time.sleep(5)
#     # driver.maximize_window()
#     pagesNumbers = soup.find('div', {'class': 'pages_container_top'})
#     data = []
#     try:
#         p_no = pagesNumbers.find('strong').text
#         pages = ''
#         for n in range(len(p_no)):
#             if p_no[n] != ',':
#                 pages += p_no[n]
#         print(int(pages))
#         pages = int(pages)
#         pg = np.arange(1, (pages/30) + 1, 1)
#         for page in pg:
#             driver.get(path+ '/' + str(page))
#             soup1 = BeautifulSoup(driver.page_source, 'html.parser')
#             listing = soup1.find('div', {'id':'listings'})
#             # print(listing)
            
#             for div in listing.find_all('div', {'class':'company'}):
#                 try:
#                     for h4 in div.find_all('h4'):
#                         company_name = h4.text
#                         for link in h4.find_all('a', href = True):
#                             print(f"https://www.yello.ae/{link['href']}")
#                             data.append(['Public & Social Services in UAE','Best Schools in UAE',company_name, f"https://www.yello.ae/{link['href']}"])
#                             df = pd.DataFrame(data,columns=['Category','SubCategory','Company Name', 'Companies url'])
#                             df.to_csv('CatSubCatComUrls.xlsx')
#                 except:
#                     company_name = 'Null'
#     except:
#         pass
        
        


driver.quit()