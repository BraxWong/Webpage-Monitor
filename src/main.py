import emailSender
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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
try:
    driver.get(url)
    #Wait 30 seconds for the browser to load before getting info
    time.sleep(30)
    items = driver.find_elements(By.CLASS_NAME, 'ItemPreview-commonInfo')
    for item in items:
        #TODO: Should write to file to check if all items are the same 
        itemName = item.find_element(By.CLASS_NAME, 'ItemPreview-itemName').text
        itemPrice = item.find_element(By.CLASS_NAME, 'Tooltip-link').text
        print(itemName, itemPrice)
    while True:
        continue
except:
    print("Something went wrong")
    # emailSender.sendEmail(emailAddress, password, "Warning!! Monitor Has Been Terminated", "An error has taken place and the program has terminated. Please reboot as soon as possible") 





