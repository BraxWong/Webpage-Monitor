from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

class Selenium_Config: 
    def __init__(self):
        self.options = uc.ChromeOptions()
        self.options.headless = False 
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
        self.driver = uc.Chrome(options=self.options)

    def quit_session(self):
        self.driver.quit()