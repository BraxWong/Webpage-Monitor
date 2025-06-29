import JSON as j
from Selenium_Config import Selenium_Config
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

skinport_unusual_url = 'https://skinport.com/tf2/market?quality=12&sort=date&order=desc'
skinport_key_url = 'https://skinport.com/tf2/market?cat=Tool&item=Mann+Co.+Supply+Crate+Key&sort=price&order=asc'
skinport_seller_fee = 0.88
item_list, price_list, item_link_list =[],[],[]
selenium_config = Selenium_Config()

def get_key_price():
    selenium_config.driver.get(skinport_key_url)
    time.sleep(5)
    items = selenium_config.driver.find_elements(By.CLASS_NAME, 'ItemPreview-content')
    return float(items[0].find_element(By.CLASS_NAME, 'Tooltip-link').text.removeprefix('£')) * skinport_seller_fee

def get_unusual_items_info():
    selenium_config.driver.get(skinport_unusual_url)
    time.sleep(5)
    items = selenium_config.driver.find_elements(By.CLASS_NAME, 'ItemPreview-content') 
    for item in items:
        item_name = item.find_element(By.CLASS_NAME, 'ItemPreview-itemName').text
        item_price = item.find_element(By.CLASS_NAME, 'Tooltip-link').text
        item_link = item.find_element(By.CLASS_NAME, 'ItemPreview-link').get_attribute("href")
        item_list.append(item_name)
        price_list.append(item_price)
        item_link_list.append(item_link)

while True:
    try:
        get_unusual_items_info()
        key_price = get_key_price()
        j.check_database(item_list, price_list, item_link_list, skinport_seller_fee, key_price)
        while True:
            continue
    except Exception as e:
        print(e)