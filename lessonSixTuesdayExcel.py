# #libraries need for my code to do the job
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
 
# #telling Chromedriver to work with Chrome Browser
# driver = webdriver.Chrome()

# driver.get('https://www.politiaromana.ro/en/most-wanted&page=1')
# driver.maximize_window()
# driver.execute_script(("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(10)

# # Go to - https://www.politiaromana.ro/en/most-wanted&page=1 and Extract Name + DOB from every single page of the web site
# urls = ['https://www.politiaromana.ro/en/most-wanted&page=1',
#          'https://www.politiaromana.ro/en/most-wanted&page=2',
#          'https://www.politiaromana.ro/en/most-wanted&page=3',
#          'https://www.politiaromana.ro/en/most-wanted&page=4',
#          'https://www.politiaromana.ro/en/most-wanted&page=5',
#          'https://www.politiaromana.ro/en/most-wanted&page=6',
#          'https://www.politiaromana.ro/en/most-wanted&page=7'
#          ]

# #tell the program which page to visit
# for link in urls:
#     driver.get(link)
#     time.sleep(3)

#     for i in range(2,16):
#         if i == 4 or i == 7 or i == 10 or i ==13:
#             continue
#         x = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         x = x + str(i) + ']/div[2]/h3/a'
#         name = driver.find_element(By.XPATH,x).text

#         y = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         y = y + str(i) + ']/div[2]/p/span'
#         bdays = driver.find_element(By.XPATH, y).text
#         print(name + ' ! '+ bdays)


####______________________________________________________________________________________________________________  

# #libraries need for my code to do the job
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# #telling Chromedriver to work with Chrome Browser
# driver = webdriver.Chrome()

# #tell the program which page to visti 
# # Go to - https://www.politiaromana.ro/en/most-wanted&page=1 and Extract Name + DOB from every single page of the web site

# for i in range(1, 8):
#     url = 'https://www.politiaromana.ro/en/most-wanted&page='
#     url = url + str(i)
#     driver.get(url)
#     time.sleep(5)
 
# #tell the scritp to maximze the web page
#     driver.maximize_window()
 
# #scroll down to show the full content of a web page
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


         
# #tell the program which page to visit
#     for a in range (2, 16):
#         if a == 4 or a == 7 or a == 10 or a == 13:
#             continue
#         x = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         x = x + str(a) + ']/div[2]/h3/a'
#         name = driver.find_element(By.XPATH,x).text

#         y = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         y = y + str(a) + ']/div[2]/p/span'
#         bdays = driver.find_element(By.XPATH, y).text
        
#         print(name + ' ! '+ bdays)

#####_____________________________________________________________________________________________________________________

# ## Login to a website
# #libraries need for my code to do the job
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# #telling Chromedriver to work with Chrome Browser
# driver = webdriver.Chrome()

# #tell the program which page to visti 
# url = driver.get('https://redmine.c6-intelligence.com/login')
# driver.get(url)
# time.sleep(10)

# username = driver.find_element(By.XPATH, '//*[@id="username"]')
# password = driver.find_element(By.XPATH, '//*[@id="password"]')
# username.send_keys('username@mail.com')
# password.send_keys('login123')

# login = driver.find_element(By.XPATH, '//*[@id="login-form"]/form/table/tbody/tr[4]/td[2]/input').click()
# time.sleep(10)



####______________________________________________________________________________________________________________

#libraries need for my code to do the job
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
 
#telling Chromedriver to work with Chrome Browser
driver = webdriver.Chrome()

# Creating/Opening a file to write te data in. Please change the pasth to the correct csv file on your computer
with open(r'C:\Users\Karolina.Gugudis\Desktop\China wanted.csv', 'w', encoding="utf-8") as f:  # w is for writing a new file
    f.write('name!dob')

driver.get('https://www.politiaromana.ro/en/most-wanted&page=1')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

# Go to - https://www.politiaromana.ro/en/most-wanted&page=1 and Extract Name + DOB from every single page of the web site
urls = ['https://www.politiaromana.ro/en/most-wanted&page=1',
         'https://www.politiaromana.ro/en/most-wanted&page=2',
         'https://www.politiaromana.ro/en/most-wanted&page=3',
         'https://www.politiaromana.ro/en/most-wanted&page=4',
         'https://www.politiaromana.ro/en/most-wanted&page=5',
         'https://www.politiaromana.ro/en/most-wanted&page=6',
         'https://www.politiaromana.ro/en/most-wanted&page=7'
         ]

#tell the program which page to visit
for link in urls:
    driver.get(link)
    time.sleep(3)

    for i in range(2,16):
        if i == 4 or i == 7 or i == 10 or i ==13:
            continue
        x = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
        x = x + str(i) + ']/div[2]/h3/a'
        name = driver.find_element(By.XPATH,x).text

        y = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
        y = y + str(i) + ']/div[2]/p/span'
        bdays = driver.find_element(By.XPATH, y).text
        print(name + ' ! '+ bdays)
        with open(r'C:\Users\Karolina.Gugudis\Desktop\China wanted.csv', 'a', encoding="utf-8") as f:  # a is for appending information to the file
            f.write(name + ' ! '+ bdays  + '\n')

# Open the csv file from the Desktop, mark colum A, go to Data - Text to Columns - Next - Other - wirte te symbol ! in the space - Next - Finish



