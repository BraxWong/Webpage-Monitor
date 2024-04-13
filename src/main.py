import requests
import emailSender
from bs4 import BeautifulSoup
  
emailAddress = input("Please input your email address: ")
password = input("Please input your password: ")

while True:
    try:
        r = requests.get('https://skinport.com/tf2/market?quality=12&sort=date&order=desc', timeout=5, allow_redirects=True)
        if r.status_code != 200:
            print("Error retrieving from the website. Terminating")
            exit()
        else:
            print(f"Final URL: {r.url}")
            soup = BeautifulSoup(r.text, 'lxml')
            items = soup.find_all('div', class_ = 'CatalogPage-item CatalogPage-item--grid')
            print(items)
            emailSender.sendEmail(emailAddress, password)
    except Exception as e:
        print("Error retrieving from the website. Terminating")
        exit()




