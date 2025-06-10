from selenium import webdriver
from selenium.webdriver.common.by import By
from Selenium_Config import Selenium_Config 
import time
from unusualToCodeMap import UnusualToCodeMode


def getLink(itemName, particle):
    itemNameList = itemName.strip().split(" ")
    itemName = ""
    for i in range(len(itemNameList)):
        itemName += itemNameList[i]
        if i != len(itemNameList) - 1:
            itemName += "%20"
    url = f'https://next.backpack.tf/classifieds?itemName={itemName}&quality=5&particle={particle}'
    if "Strange" in itemName:
        url += '&elevatedQuality=11'
        url = url.replace("Strange%20%20",'')
    return url

def getUnusualIndex(itemName):
    unusualMap = UnusualToCodeMode()
    for key, value in unusualMap.map.items():
        if key in itemName:
            return [itemName.replace(key,''),value]
    return []

def getItemPrice(item_name, itemPrice):
    #selenium_config = Selenium_Config()
    linkInfo = getUnusualIndex(item_name)
    print(linkInfo)
    url = getLink(linkInfo[0], linkInfo[1])
    print(url)
    #selenium_config.driver.get(url)
    #Wait 30 seconds for the browser to load before getting info
    #time.sleep(10)
    #items = selenium_config.driver.find_element(By.CLASS_NAME, 'item__price').text
    #if float(items) * 1.2 > float(itemPrice):
        #return True
    #time.sleep(10)
    #return False

getItemPrice(["Violent Violets Taunt: Mourning Mercs"],["13.21"])

