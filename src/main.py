
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
from urllib.request import urlopen, Request 
  
url = Request('https://skinport.com/tf2/market?quality=12&sort=date&order=desc', 
              headers={'User-Agent': 'Mozilla/5.0'}) 
  
response = urlopen(url).read() 
  
currentHash = hashlib.sha224(response).hexdigest() 
time.sleep(10) 
while True: 
    try: 
        response = urlopen(url).read() 
  
        currentHash = hashlib.sha224(response).hexdigest() 
  
        time.sleep(30) 
  
        response = urlopen(url).read() 
  
        newHash = hashlib.sha224(response).hexdigest() 
  
        if newHash == currentHash: 
            continue
  
        else: 
            response = urlopen(url).read() 
  
            currentHash = hashlib.sha224(response).hexdigest() 
  
            time.sleep(30) 
            continue
  
    except Exception as e: 
        print("error") 
