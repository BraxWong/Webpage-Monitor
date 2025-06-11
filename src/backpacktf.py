from selenium.webdriver.common.by import By
from Selenium_Config import Selenium_Config 
import time
from unusualToCodeMap import UnusualToCodeMode

def getLink(item_name, particle):
    item_name_list = item_name.strip().split(" ")
    item_name = ""
    for i in range(len(item_name_list)):
        itemName += item_name_list[i]
        if i != len(item_name_list) - 1:
            itemName += "%20"
    url = f'https://next.backpack.tf/classifieds?itemName={item_name}&quality=5&particle={particle}'
    if "Strange" in item_name:
        url += '&elevatedQuality=11'
        url = url.replace("Strange%20%20",'')
    return url

def getUnusualIndex(item_name):
    unusual_map = UnusualToCodeMode()
    for key, value in unusual_map.map.items():
        if key in item_name:
            return [item_name.replace(key,''),value]
    return []

def getItemPrice(item_name):
    selenium_config = Selenium_Config()
    link_info = getUnusualIndex(item_name)
    url = getLink(link_info[0], link_info[1])
    selenium_config.driver.get(url)
    #Wait 10 seconds for the browser to load before getting info
    time.sleep(10)
    buy_orders = selenium_config.driver.find_elements(By.CLASS_NAME, 'classifieds__column')[1]
    return buy_orders.find_element(By.CLASS_NAME, 'item__price').text.replace(' keys','') 

def calculate_profit(marketplace_item_price, marketplace_key_price, marketplace_seller_fee, bptf_price):
    key_price_after_fees = marketplace_key_price * marketplace_seller_fee
    return bptf_price * key_price_after_fees - marketplace_item_price