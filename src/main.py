import emailSender
from selenium import webdriver
import time
emailAddress = input("Please input your email address: ")
password = input("Please input your password: ")

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
url = 'https://skinport.com/tf2/market?quality=12&sort=date&order=desc'
driver = webdriver.Chrome(options=options)
try:
    driver.get(url)
    while True:
        pass
except:
    emailSender.sendEmail(emailAddress, password, "Warning!! Monitor Has Been Terminated", "An error has taken place and the program has terminated. Please reboot as soon as possible") 





