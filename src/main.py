import emailSender
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time
import json

def checkIfItemMatch(itemList, priceList, emailAddress, password):
    with open("database.json", "r+", encoding='utf-8') as file:
        print("Opening the file")
        file_data = json.load(file)
        index = 0
        fileWiped = False
        itemString = ""
        for item in file_data["items"]:
            if item["item name"] != itemList[index]:
                print("New item spotted. Clearing the database")
                itemString = itemList[index] + " " + str(priceList[index])
                if index==0:
                    file_data["items"].clear()
                    file.seek(0)
                    file.truncate()
                    json.dump(file_data, file, indent = 2, ensure_ascii=False)
                    fileWiped = True
                    break
            index +=1

        if fileWiped:
            print("Adding item to the database")
            for index in range(len(itemList)):
                file_data["items"].append({"item name": itemList[index] , 
                                            "price": priceList[index]
                                        })
            file.seek(0)
            json.dump(file_data, file, indent = 2, ensure_ascii=False)
            emailSender.sendEmail(emailAddress, password, "New item on skinport!!!", itemString)
            
        file.truncate()
        file.close()



emailAddress = input("Please input your email address: ")
password = input("Please input your password: ")


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.binary_location = r"chromedriver" 
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
        run_on_insecure_origins= False
        )

while True:
    try:
        driver.get(url)
        #Wait 30 seconds for the browser to load before getting info
        time.sleep(10)
        items = driver.find_elements(By.CLASS_NAME, 'ItemPreview-commonInfo')
        itemList, priceList=[],[]
        for item in items:
            itemName = item.find_element(By.CLASS_NAME, 'ItemPreview-itemName').text
            itemPrice = item.find_element(By.CLASS_NAME, 'Tooltip-link').text
            itemList.append(itemName)
            priceList.append(itemPrice)
        print("Going into checkIfItemMatch()")
        checkIfItemMatch(itemList, priceList, emailAddress, password)
        print("bout to go to sleep")
        time.sleep(60)
    except:
        # emailSender.sendEmail(emailAddress, password, "Warning!! Monitor Has Been Terminated", "An error has taken place and the program has terminated. Please reboot as soon as possible")
        break


