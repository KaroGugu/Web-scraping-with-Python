# a = 20
# b = 30.5
# combination = round(a + b)

# for i in range(1, combination + 1):
#     print(i)

#### _________________________________________________________________________    

# #libraries need for my code to do the job
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
 
# #telling Chromedriver to work with Chrome Browser
# driver = webdriver.Chrome()
 
# #tell the program which page to visti 
# driver.get('https://crimestoppers-uk.org/give-information/most-wanted')
 
# time.sleep(10)
 
# #tell the scritp to maximze the web page
# driver.maximize_window()
 
# #scroll down to show the full content of a web page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
# for i in range(1,17):
 
#     x = '//*[@id="main"]/main/article/div[3]/div[1]/div[2]/div['
#     x = x + str(i) + ']/div/div/span[1]'
#     name = driver.find_element(By.XPATH,x).text
#     print(name)


####__________________________________________________________________________________________

#libraries need for my code to do the job
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
#telling Chromedriver to work with Chrome Browser
driver = webdriver.Chrome()
 
#tell the program which page to visti 
driver.get('https://efoia.bis.doc.gov/index.php/7-electronic-foia/227-export-violations')
 
time.sleep(10)
 
#tell the scritp to maximze the web page
driver.maximize_window()
 
#scroll down to show the full content of a web page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
for i in range(3,964):
    x = '//*[@id="maincontent"]/div[2]/div[3]/table/tbody/tr['
    x = x + str(i) + ']'
    name = driver.find_element(By.XPATH,x).text
    
    y = '//*[@id="maincontent"]/div[2]/div[3]/table/tbody/tr['
    y = y + str(i) + ']/td[1]'
    caseId = driver.find_element(By.XPATH, y).text

    z = '//*[@id="maincontent"]/div[2]/div[3]/table/tbody/tr['
    z += str(i) + ']/td[3]'
    date = driver.find_element(By.XPATH, z).text
    
    print(caseId + '!' + name + '!' + date)

# case ID, name, date
# x = '//*[@id="maincontent"]/div[2]/div[3]/table/tbody/tr['
# x = x + str(i) + ']'