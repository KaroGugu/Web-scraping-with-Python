### functions of Selenium to find elements in a webpage
## driver.get()
## someTextFromPage = driver.find_element(By.XPATH, 'sdadsa').text
## someUrl = driver.find_element(By.XPATH, 'sdadsa').get_attribue('href')
## someProfilePhoto = driver.find_element(By.XPATH, 'sdadsa').get_attribue('src')

## XPATH helper extension in Chrome

## function to click on a button
## nextButton = driver.get_element(By.XPATH, '//*[@id="paginationPanel"]/div/div/ul/li[9]/a/svg').click()


## more advanced way to find elements in a webpage - also when on page 2,3... the url doesn't change
## https://www.interpol.int/en/How-we-work/Notices/Red-Notices/View-Red-Notices
## with Inspect - Copy Selector
## #noticesResultsItemList > div:nth-child(1) > div > div > div.redNoticeItem__text > div.redNoticeItem__labelText > a
## class name
## name = drive.find_element(By.CLASS_NAME,'redNoticeItem__text')



## there are websites that don't work with Selekium 

## protected websites from scraping
## https://www.fntt.lt/en/international-financial-sanctions/4254
## ask google: How to scrape cloudflare protected sites with selenium
## https://stackoverflow.com/questions/68289474/selenium-headless-how-to-bypass-cloudflare-detection-using-selenium
## import undetected_chromedriver as uc
## from selenium import webdriver


