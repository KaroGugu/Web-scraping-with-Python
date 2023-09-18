# # # for a in range(1,11):
# # #     print(a) # 1,2,3...10

####_____________________________________________________________________________________
# # # Giving errors
# # from selenium.webdriver import Chrome
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # import time
# # from selenium.common.exceptions import NoSuchElementException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
 
# # # Set the path to the Chrome driver executable
# # driver_path = r'C:\Users\Karolina.Gugudis\Desktop\chromedriver.exe'
 
# # # Create a new instance of the Chrome driver
# # service = Service(executable_path=driver_path)
# # driver = Chrome(service=service)

# # driver.get('https://www.google.com/')
# # time.sleep(20)


####____________________________________________________________________________
# ## shorter code - working
# # from selenium import webdriver
# # import time
 
# # driver = webdriver.Chrome()
 
# # driver.get('https://www.google.com/')
 
# # time.sleep(10)

####__________________________________________________________________
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
 
# # driver = webdriver.Chrome()
 
# # driver.get('https://crimestoppers-uk.org/give-information/most-wanted')
 
# # time.sleep(10)


####________________________________________________________________________________
# # #libraries need for my code to do the job
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
 
# # #telling Chromedriver to work with Chrome Browser
# # driver = webdriver.Chrome()
 
# # #tell the program which page to visit 
# # driver.get('https://crimestoppers-uk.org/give-information/most-wanted')
 
# # #tell the scritp to maximze the web page
# # driver.maximize_window()
 
# # #scroll down to show the full content of a web page
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
# # time.sleep(20)


####_________________________________________________________________________________________ 
##libraries need for my code to do the job
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
#telling Chromedriver to work with Chrome Browser
driver = webdriver.Chrome()
 
#tell the program which page to visti 
driver.get('https://crimestoppers-uk.org/give-information/most-wanted')
 
time.sleep(5)
 
#tell the scritp to maximze the web page
driver.maximize_window()
 
#scroll down to show the full content of a web page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# go to web page, right click Inspect, select an element, right click Copy - Copy Xpath
name1 = driver.find_element(By.XPATH, '//*[@id="main"]/main/article/div[3]/div[1]/div[2]/div[1]/div/div/span[1]').text
 
print(name1)  # Alex MALE - Wanted
 
name2 = driver.find_element(By.XPATH, '//*[@id="main"]/main/article/div[3]/div[1]/div[2]/div[5]/div/div/span[1]').text
 
print(name2) # John James JONES - Wanted
 
time.sleep(30)

