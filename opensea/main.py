from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

def get_links():
    # # driver = webdriver.Firefox()
    driver.get("https://opensea.io/collection/jordannft")
    time.sleep(10)
    driver.maximize_window()
    links = []
    s = 300
    for _ in range(400, 0, -1):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # time.sleep(2)
        main_div = soup.find("div", {"class":"AssetSearchView--results collection--results"})
        links.extend(
            f"https://opensea.io//{a['href']}"
            for a in main_div.find_all(
                'a',
                {
                    'class': 'styles__StyledLink-sc-l6elh8-0 ekTmzq Asset--anchor'
                },
                href=True,
            )
        )

        driver.execute_script(f"window.scrollTo(0, {s})")
        s += 200
        print(set(links))
        print(len(set(links)))


    print(set(links))
    print(len(set(links)))
    df = pd.DataFrame(set(links),columns=['URL'])
    df.to_excel("Shahid_Sahab.xlsx", index=False)
    
    
def reload_button():
    df = pd.read_excel('359.xlsx')
    links = df.iloc[:,-1]
    # print(links)
    links = list(links)
    # print(links)
    for page in range(300,len(links)):
        # print(links)
        driver.get(links[page])
        time.sleep(2)
        # Blockreact__Block-sc-1xf18x6-0 Buttonreact__StyledButton-sc-glfma3-0 bhqEJb jdSrqf ButtonGroupreact__StyledButton-sc-1skvztv-0 eztnHW
        
        btn = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div[2]/div/section[1]/div/div[2]/div/button[1]')
        btn.click()
        time.sleep(2)
        print(page)