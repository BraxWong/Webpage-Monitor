from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
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
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.binary_location = r"chromedriver" 
    options.headless= True
    linkInfo = getUnusualIndex(item_name)
    url = getLink(linkInfo[0], linkInfo[1])
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
    driver.get(url)
    #Wait 30 seconds for the browser to load before getting info
    time.sleep(10)
    items = driver.find_element(By.CLASS_NAME, 'item__price').text
    if float(items) * 1.2 > float(itemPrice):
        return True
    time.sleep(10)
    return False


