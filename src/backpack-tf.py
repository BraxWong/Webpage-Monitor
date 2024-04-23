from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

def getLink(itemName, particle):
    itemNameList = itemName.strip().split(" ")
    itemName = ""
    for i in range(len(itemNameList)):
        itemName += itemName[i]
        if i != len(itemName) - 1:
            itemName += "%20"

    return f'https://next.backpack.tf/classifieds?itemName={itemName}&quality=5&particle={particle}'

def getItemPrice(item_name, particle):
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.binary_location = r"chromedriver" 
    options.headless = True
    url = getLink(item_name, particle)
    driver = webdriver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            un_on_insecure_origins= False,
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
            checkIfItemMatch(itemList, priceList)
            while True:
                continue
        except:
            print("Something went wrong")
            # emailSender.sendEmail(emailAddress, password, "Warning!! Monitor Has Been Terminated", "An error has taken place and the program has terminated. Please reboot as soon as possible") 


