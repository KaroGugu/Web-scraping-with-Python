#### https://hatebin.com/qvjoqfqiqz - the code
### To get all members' name from Sharjah Executive Council

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
  
driver = webdriver.Chrome()
#Creating/Opening a file to write the data in. Please change the path to the correct file on your computer.
with open(r'C:\Users\Karolina.Gugudis\Desktop\Sharjah Executive Council', 'w', encoding="utf-8") as f: # w is for writing a new file
    f.write('Members of Executive Council \n')
    
driver.get('https://ec.shj.ae/en/executive-council/')
 
driver.maximize_window()
 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

    
for i in range(2,5):
    x = '//*[@id="content"]/div/div/div/div/section[2]/div[2]/div['
    x = x + str(i) + ']/div/h3'
        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[2]/div/h3
        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[3]/div/h3
        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[4]/div/h3
    name = driver.find_element(By.XPATH,x).text 
    print(name)
    
for y in range(1,28):
    z = '//*[@id="content"]/div/div/div/div/section[2]/div[2]/div[5]/div['
    z = z + str(y) + ']/div[2]/h3'

        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[5]/div[1]/div[2]/h3
        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[5]/div[9]/div[2]/h3
        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[5]/div[2]/div[2]/h3
        # //*[@id="content"]/div/div/div/div/section[2]/div[2]/div[5]/div[27]/div[2]/h3

    name = driver.find_element(By.XPATH,z).text 
    print(name)
    
    with open(r'C:\Users\Karolina.Gugudis\Desktop\Sharjah Executive Council.csv', 'a', encoding="utf-8") as f: # a is for appending information to the file
        f.write(name + '\n')
 
print('the job is done')