# ## Give all the names from all the pages
# #libraries need for my code to do the job
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
 
# #telling Chromedriver to work with Chrome Browser
# driver = webdriver.Chrome()
 
# #tell the program which page to visit 
# driver.get('https://eumostwanted.eu/')
 
# time.sleep(10)
 
# #tell the scritp to maximze the web page
# driver.maximize_window()

# time.sleep(10)

# # go to web page, right click Inspect, select an element, right click Copy - Copy Xpath
# name1 = driver.find_element(By.XPATH, '//*[@id="block-eumwfoundationtheme-content"]/div/div/div/div[1]/div[1]/div[3]/span').text
# print(name1)  # HAREDIN, FEJZULLA

# name2 = driver.find_element(By.XPATH, '//*[@id="block-eumwfoundationtheme-content"]/div/div/div/div[1]/div[4]/div[4]/span').text
# print(name2)  # ŻYŁA, KAMIL

# name3 = driver.find_element(By.XPATH, '//*[@id="block-eumwfoundationtheme-content"]/div/div/div/div[1]/div[48]/div[3]/span').text
# print(name3) # KALASUNAS, Edgaras

# time.sleep(10)


####__________________________________________________________

#libraries need for my code to do the job
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
#telling Chromedriver to work with Chrome Browser
driver = webdriver.Chrome()
 
#tell the program which page to visti 
driver.get('https://crimestoppers-uk.org/give-information/most-wanted')
 
time.sleep(10)
 
#tell the scritp to maximze the web page
driver.maximize_window()
 
#scroll down to show the full content of a web page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
for i in range(1,17):
 
    x = '//*[@id="main"]/main/article/div[3]/div[1]/div[2]/div['
    x = x + str(i) + ']/div/div/span[1]'
    name = driver.find_element(By.XPATH,x).text
    print(name)


# x = '//*[@id="main"]/main/article/div[3]/div[1]/div[2]/div[1'
# x += str(i)
# x += ']/div/div/span[1]'
time.sleep(10)
