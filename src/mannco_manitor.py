import JSON as j
from Selenium_Config import Selenium_Config
from selenium.webdriver.common.by import By
import time
import subprocess
from sys import platform
from Enum import Site_Classifications

mannco_unusual_url = 'https://mannco.store/tf2?&quality=Unusual&page=1&age=DESC'
mannco_key_url = 'https://mannco.store/item/440-mann-co-supply-crate-key'
mannco_seller_fee = 0.95
item_list,price_list,item_link_list=[],[],[]
selenium_config = Selenium_Config()

def get_key_price():
    selenium_config.driver.get(mannco_key_url)
    time.sleep(5)
    key_price = float(selenium_config.driver.find_element(By.CLASS_NAME, 'ecurrency').text.removeprefix('$')) * mannco_seller_fee
    return key_price 

def get_unusual_items_info():
    selenium_config.driver.get(mannco_unusual_url)
    time.sleep(5)
    items = selenium_config.driver.find_elements(By.CLASS_NAME, 'item-info')
    for item in items:
        unusual_effect = item.find_element(By.CLASS_NAME, "item-name").text.removeprefix('★ ').replace('\n','')
        if "Uncraftable" not in unusual_effect and '(' not in unusual_effect:
            hat_name = item.find_element(By.CLASS_NAME, 'item-name-description').text.replace("Unusual",'')
            price = item.find_element(By.CLASS_NAME, 'item-price').text.removeprefix('$ ')
            item_list.append(unusual_effect.replace(hat_name,'').replace("Unusual",'') + hat_name)
            price_list.append(price)
            unusual_effect = unusual_effect.replace(hat_name,'').replace(' ','-').replace('Unusual','-Unusual')
            unusual_effect += hat_name.replace(' ','-')
            unusual_effect = unusual_effect.replace(':','').replace('\'','')
            item_link_list.append(f"https://mannco.store/item/440-{unusual_effect}")
    selenium_config.quit_session()

def run():
    while True:
        try:
            key_price = get_key_price()
            get_unusual_items_info()
            j.check_database(item_list, price_list, item_link_list, mannco_seller_fee, key_price, Site_Classifications.MANNCO)
        except Exception as e:
            print(f"Mannco Error message: {e}")
            if platform == "linux":
                subprocess.run(f'cd src && ./DiscordWebhook "{e}"')
            else:
                subprocess.run(f'cd src && .\\DiscordWebhook.exe "{e}"')
            break