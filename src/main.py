import JSON as j
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time


url = 'https://skinport.com/tf2/market?quality=12&sort=date&order=desc'
options = uc.ChromeOptions()
options.headless = False 
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
driver = uc.Chrome(options=options)

while True:
        try:
            driver.get(url)
            #Wait 30 seconds for the browser to load before getting info
            time.sleep(10)
            items = driver.find_elements(By.CLASS_NAME, 'ItemPreview-commonInfo')
            itemList, priceList, item_link_list =[],[],[]
            for item in items:
                itemName = item.find_element(By.CLASS_NAME, 'ItemPreview-itemName').text
                itemPrice = item.find_element(By.CLASS_NAME, 'Tooltip-link').text
                item_link = "https://skinport.com/" + item.find_element(By.CLASS_NAME, 'ItemPreview-link').get_attribute("href")
                itemList.append(itemName)
                priceList.append(itemPrice)
                item_link_list.append(item_link)
            j.check_database(["ITEM1", "ITEM2"],[13, 14],["URL1", "URL2"])
            while True:
                continue
        except:
            print("Something went wrong")
