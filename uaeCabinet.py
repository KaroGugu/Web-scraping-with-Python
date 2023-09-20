#### https://hatebin.com/uqctvspvbq - the code
### To get all members' name from UAE Cabinet


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Chrome()

#Creating/Opening a file to write the data in. Please change the path to the correct file on your computer.
with open(r'C:\Users\Karolina.Gugudis\Desktop\UAE Cabinet.csv', 'w', encoding="utf-8") as f: # w is for writing a new file
    f.write('Cabinet Members \n')
    
driver.get('https://uaecabinet.ae/en/cabinet-members?page=1')
 
driver.maximize_window()
 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)
allprofileshyperlinks=['https://uaecabinet.ae/en/cabinet-members?page=1',
     'https://uaecabinet.ae/en/cabinet-members?page=2',
     'https://uaecabinet.ae/en/cabinet-members?page=3',
     'https://uaecabinet.ae/en/cabinet-members?page=4',
     'https://uaecabinet.ae/en/cabinet-members?page=5',
     'https://uaecabinet.ae/en/cabinet-members?page=6',
     'https://uaecabinet.ae/en/cabinet-members?page=7']


for link in allprofileshyperlinks:
    driver.get(link)
    time.sleep(1)
    
    for i in range(1,6):
        x = '//*[@id="homeWrapper"]/div/div[2]/div/div[2]/div/div/div[1]/div['
        x = x + str(i) + ']/div[2]/h3'
        # //*[@id="homeWrapper"]/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/h3
        # //*[@id="homeWrapper"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/h3
        profileurl = driver.find_element(By.XPATH,x).text 
        print(profileurl)
 
        
        with open(r'C:\Users\Karolina.Gugudis\Desktop\UAE Cabinet.csv', 'a', encoding="utf-8") as f: # a is for appending information to the file
            f.write(profileurl + '\n')
 
print('the job is done')