### pastebin code: https://pastebin.pl/view/a838025a
### Browse through all the 10 pages on the web-site 
## https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=1
## collect/print all the hyperlinks that lead to each individual profile in terminal/CSV
## Concatenate the collected urls and go through each profile (you can create another program, by just looping through the list) 
## Collect the below information (if existent on each profile) and print it in CSV file
## name, DOB, nationality, address,start and end date, case referrence

## Desired output:
## profileUrl + ‘!’ + name + ‘!’ + dob + ‘!’ + nationality + ‘!’ + address + ‘!’  + startDate + ‘!’ + endDate  + ‘!’ + caseReference + ‘\n’

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Chrome()

# Creating/Opening a file to write te data in. Please change the pasth to the correct csv file on your computer
with open(r'C:\Users\Karolina.Gugudis\Desktop\Find and update company info.csv', 'w', encoding="utf-8") as f:  # w is for writing a new file
    f.write('profilesurls \n')


driver.get('https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

urls = ['https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=1',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=2',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=3',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=4',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=5',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=6',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=7',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=8',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=9',
        'https://find-and-update.company-information.service.gov.uk/register-of-disqualifications/A?page=10'
        ]

for link in urls:
    driver.get(link)
    time.sleep(3)

    for i in range(2, 52): # the hyperlink of the names to each profile
        x = '//*[@id="search-container"]/div[1]/table/tbody/tr['
        x = x + str(i) + ']/td[1]/a'
        # //*[@id="search-container"]/div[1]/table/tbody/tr[2]/td[1]/a
        # //*[@id="search-container"]/div[1]/table/tbody/tr[3]/td[1]/a
        # //*[@id="search-container"]/div[1]/table/tbody/tr[4]/td[1]/a
        # //*[@id="search-container"]/div[1]/table/tbody/tr[5]/td[1]/a
        # //*[@id="search-container"]/div[1]/table/tbody/tr[51]/td[1]/a
        # //*[@id="search-container"]/div[1]/table/tbody/tr[25]/td[1]/a - last page # 10

        try:
            profileurl = driver.find_element(By.XPATH,x).get_attribute('href')  
        except NoSuchElementException:
            profileurl = 'no name'
        print(profileurl)

        with open(r'C:\Users\Karolina.Gugudis\Desktop\Find and update company info.csv', 'a', encoding="utf-8") as f: # a is for appending information to the file
            f.write(profileurl + '\n')
    
print('the job is done')
