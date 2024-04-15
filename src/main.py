import emailSender
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import time
import json

def checkIfItemMatch(itemList, priceList, discountList):
    with open("database.json", "r+", encoding='utf-8') as file:
        file_data = json.load(file)
        index = 0
        for item in file_data["items"]:
            if item["item name"] != itemList[index]:
                print("Could not find the item")
                if index==0:
                    print("Index is 0 ... Clearing the database")
                    item["items"].clear()
                else:
                    #TODO: Check if the percentage is over 25%. If so, send an email
                    print("Adding item to the database")
                    item["items"].append({"item name": itemList[index] , 
                                          "price": priceList[index],
                                          "discount": discountList[index]
                                          })
            print(itemList[index], priceList[index])
            index+=1



# emailAddress = input("Please input your email address: ")
# password = input("Please input your password: ")

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.headless = True
url = 'https://skinport.com/tf2/market?quality=12&sort=date&order=desc'
driver = webdriver.Chrome(options=options)
stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
try:
    driver.get(url)
    #Wait 30 seconds for the browser to load before getting info
    time.sleep(30)
    items = driver.find_elements(By.CLASS_NAME, 'ItemPreview-commonInfo')
    print("Found itemPreview")
    itemList, priceList, discountList=[],[],[]
    for item in items:
        itemName = item.find_element(By.CLASS_NAME, 'ItemPreview-itemName').text
        print("Found itemName")
        itemPrice = item.find_element(By.CLASS_NAME, 'Tooltip-link').text
        print("Found itemPrice")
        itemDiscount = item.find_element(By.CLASS_NAME, 'GradientLabel ItemPreview-discount')
        print("Find item discount")
        if itemDiscount.is_displayed():
            itemDiscount = item.find_elements(By.CLASS_NAME, 'GradientLabel ItemPreview-discount')
            print("Found item discount")
            for discount in itemDiscount: 
                percentage = discount.find_element(By.TAG_NAME, 'span').text
                print("Found the real discount")
                discountList.append(percentage)
        else:
            discountList.append('- 0%')
        itemList.append(itemName)
        priceList.append(itemPrice)
    checkIfItemMatch(itemList, priceList, discountList)
    while True:
        continue
except:
    print("Something went wrong")
    # emailSender.sendEmail(emailAddress, password, "Warning!! Monitor Has Been Terminated", "An error has taken place and the program has terminated. Please reboot as soon as possible") 



