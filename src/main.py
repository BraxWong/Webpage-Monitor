
#   ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#   ┃                                                                         ┃
#   ┃             The following code is created by geeksforgeeks.             ┃
#   ┃                            Please check out                             ┃
#   ┃ https://www.geeksforgeeks.org/python-script-to-monitor-website-changes/ ┃
#   ┃                                                                         ┃
#   ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

import time 
import hashlib 
import emailSender
import ssl

from urllib.request import urlopen, Request 
  
url = Request('https://skinport.com/tf2/market?quality=12&sort=date&order=desc',
              headers={'User-Agent': 'Mozilla/5.0'})
  
emailAddress = input("Please input your email address: ")
password = input("Please input your password: ")

response = urlopen(url, context=ssl._create_unverified_context()).read()
  
currentHash = hashlib.sha224(response).hexdigest() 
time.sleep(10) 
while True: 
    try: 
        response = urlopen(url).read() 
  
        currentHash = hashlib.sha224(response).hexdigest() 
  
        time.sleep(300) 
  
        response = urlopen(url).read() 
  
        newHash = hashlib.sha224(response).hexdigest() 
  
        if newHash == currentHash: 
            print("No Change")
            continue
  
        else:
            print("CHANGE!!!!")
            response = urlopen(url).read() 
  
            currentHash = hashlib.sha224(response).hexdigest() 
  
            emailSender.sendEmail(emailAddress, password)           

            time.sleep(300) 
            continue
  
    except Exception as e: 
        print("error") 
