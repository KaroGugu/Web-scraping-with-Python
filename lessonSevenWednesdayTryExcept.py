# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import csv
# from selenium.common.exceptions import NoSuchElementException
 
# driver = webdriver.Chrome()
# #Creating/Opening a file to write the data in. Please change the path to the correct file on your computer.
# with open(r'C:\Users\Karolina.Gugudis\Desktop\Romanian wanted.csv', 'w', encoding="utf-8") as f: # w is for writing a new file
#     f.write('name ! dob \n')
    
# driver.get('https://www.politiaromana.ro/en/most-wanted')
 
# driver.maximize_window()
 
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(10)
# allprofileshyperlinks=['https://www.politiaromana.ro/en/most-wanted&page=1',
#      'https://www.politiaromana.ro/en/most-wanted&page=2',
#      'https://www.politiaromana.ro/en/most-wanted&page=3',
#      'https://www.politiaromana.ro/en/most-wanted&page=4',
#      'https://www.politiaromana.ro/en/most-wanted&page=5',
#      'https://www.politiaromana.ro/en/most-wanted&page=6',
#      'https://www.politiaromana.ro/en/most-wanted&page=7']
 
# for link in allprofileshyperlinks:
#     driver.get(link)
#     time.sleep(1)
    
#     for i in range(2,16):
#         if i==4 or i==7 or i==10 or i==13:
#             continue
#         x = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         x = x + str(i) + ']/div[2]/h3/a'
#         try:
#             name = driver.find_element(By.XPATH,x).text
#         except NoSuchElementException:
#             name = 'no name'
 
#         y = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         y = y +str(i) + ']/div[2]/p/span'
#         try:
#             dob = driver.find_element(By.XPATH,y).text
#         except NoSuchElementException:
#             dob = 'no dob' 
        
#         print(name + '!' + dob)
#         with open(r'C:\Users\Karolina.Gugudis\Desktop\Romanian wanted.csv', 'a', encoding="utf-8") as f: # a is for appending information to the file
#             f.write(name + '!' + dob + '\n')
 
# print('the job is done')


#####__________________________________________________________________________________________________________________  

# ### To get all the hyperlinks of all profiles from the 7 pages in the website - saved to Romanian wanted Excel file
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import csv
# from selenium.common.exceptions import NoSuchElementException
 
# driver = webdriver.Chrome()
# #Creating/Opening a file to write the data in. Please change the path to the correct file on your computer.
# with open(r'C:\Users\Karolina.Gugudis\Desktop\Romanian wanted.csv', 'w', encoding="utf-8") as f: # w is for writing a new file
#     f.write('profileurl \n')
    
# driver.get('https://www.politiaromana.ro/en/most-wanted')
 
# driver.maximize_window()
 
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(10)
# allprofileshyperlinks=['https://www.politiaromana.ro/en/most-wanted&page=1',
#      'https://www.politiaromana.ro/en/most-wanted&page=2',
#      'https://www.politiaromana.ro/en/most-wanted&page=3',
#      'https://www.politiaromana.ro/en/most-wanted&page=4',
#      'https://www.politiaromana.ro/en/most-wanted&page=5',
#      'https://www.politiaromana.ro/en/most-wanted&page=6',
#      'https://www.politiaromana.ro/en/most-wanted&page=7']


# for link in allprofileshyperlinks:
#     driver.get(link)
#     time.sleep(1)
    
#     for i in range(2,16):
#         if i==4 or i==7 or i==10 or i==13:
#             continue
#         x = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div['
#         x = x + str(i) + ']/div[2]/h3/a'
#         try:
#             profileurl = driver.find_element(By.XPATH,x).get_attribute('href')  
#             # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/div[2]/h3/a - the hyperlink of the names
#             # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[3]/div[2]/h3/a - the hyperlink of the names
#         except NoSuchElementException:
#             profileurl = 'no name'
#         print(profileurl)
 
        
#         with open(r'C:\Users\Karolina.Gugudis\Desktop\Romanian wanted.csv', 'a', encoding="utf-8") as f: # a is for appending information to the file
#             f.write(profileurl + '\n')
 
# print('the job is done')


### After all hyperlinks of all profiles from the 7 pages in the website are saved to Romanian wanted Excel file, we need to concatenate them
### put ' and ,' and then on D create a string of the url using  =A2&B2&C2  
### The created anothe script that is doing the browsing and collection name, DOB, pic, address,etc

####__________________________________________________________________________________________________________ 

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Chrome()
#Creating/Opening a file to write the data in. Please change the path to the correct file on your computer.
with open(r'C:\Users\Karolina.Gugudis\Desktop\Romanian Police wanted.csv', 'w', encoding="utf-8") as f: # w is for writing a new file
    f.write('url, name, DOB, place, citizenship  \n')
    
driver.get('https://www.politiaromana.ro/en/most-wanted')
 
driver.maximize_window()
 
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
allprofiles=[
' https://www.politiaromana.ro/en/most-wanted/aurica-corado-2231992',
' https://www.politiaromana.ro/en/most-wanted/moldovan-augustin-dan-1431970',
' https://www.politiaromana.ro/en/most-wanted/ciobanu-constantin-2251985',
' https://www.politiaromana.ro/en/most-wanted/gusan-ion-17121971',
' https://www.politiaromana.ro/en/most-wanted/meshah-suhaib-abdel-naser-2911990',
' https://www.politiaromana.ro/en/most-wanted/mihaltan-ioan-lucian-3081988',
' https://www.politiaromana.ro/en/most-wanted/bolbos-adrian-1721981',
' https://www.politiaromana.ro/en/most-wanted/ciobotaru-bogdan-vasile-321991',
' https://www.politiaromana.ro/en/most-wanted/duduianu-florin-13111984',
' https://www.politiaromana.ro/en/most-wanted/boacara-florin-costin-871993',
' https://www.politiaromana.ro/en/most-wanted/memet-ali-gener-9101991',
' https://www.politiaromana.ro/en/most-wanted/orbuletu-alexandru-radu-15101991',
' https://www.politiaromana.ro/en/most-wanted/bucuresteanu-marius-iliuta-2071992',
' https://www.politiaromana.ro/en/most-wanted/pasla-marius-cristian-3151979',
' https://www.politiaromana.ro/en/most-wanted/ciuches-milut-liviu-2271993',
' https://www.politiaromana.ro/en/most-wanted/daniliuc-eugen-1441988',
' https://www.politiaromana.ro/en/most-wanted/clapon-gheorghe-1091967',
' https://www.politiaromana.ro/en/most-wanted/draniceru-oleg-981973',
' https://www.politiaromana.ro/en/most-wanted/flucsa-nicolae-sorin-291981',
' https://www.politiaromana.ro/en/most-wanted/trofim-andrei-2871973',
' https://www.politiaromana.ro/en/most-wanted/ion-emanuel-dan-13121973',
' https://www.politiaromana.ro/en/most-wanted/amegica-telu-constantin-1741985',
' https://www.politiaromana.ro/en/most-wanted/irimita-ionut-iulian-171983',
' https://www.politiaromana.ro/en/most-wanted/druta-tudor-8121985',
' https://www.politiaromana.ro/en/most-wanted/posogeanu-valentin-891981',
' https://www.politiaromana.ro/en/most-wanted/grigor-ivan-13101963',
' https://www.politiaromana.ro/en/most-wanted/gabor-gabriel-6121986',
' https://www.politiaromana.ro/en/most-wanted/omar-mukhles-3101980',
' https://www.politiaromana.ro/en/most-wanted/murtazaliev-ramazan-28111981',
' https://www.politiaromana.ro/en/most-wanted/maftei-cristian-12101969',
' https://www.politiaromana.ro/en/most-wanted/enderle-ildiko-521976',
' https://www.politiaromana.ro/en/most-wanted/iskandarani-zaher-111958',
' https://www.politiaromana.ro/en/most-wanted/kertesz-robert-1841985',
' https://www.politiaromana.ro/en/most-wanted/grad-ioan-1121964',
' https://www.politiaromana.ro/en/most-wanted/radu-stoica-anamaria-27111988',
' https://www.politiaromana.ro/en/most-wanted/bruzlea-silviu-bogdan-3041987',
' https://www.politiaromana.ro/en/most-wanted/teja-ionel-1191965',
' https://www.politiaromana.ro/en/most-wanted/mizga-valerica-2261977',
' https://www.politiaromana.ro/en/most-wanted/popescu-ovidiu-2311984',
' https://www.politiaromana.ro/en/most-wanted/gheorghe-iulian-alin-2261981',
' https://www.politiaromana.ro/en/most-wanted/zhao-junguo-2011964',
' https://www.politiaromana.ro/en/most-wanted/piclisan-claudiu-gheorghe-2711974',
' https://www.politiaromana.ro/en/most-wanted/rodideal-vasile-541961',
' https://www.politiaromana.ro/en/most-wanted/stoica-marian-1581979',
' https://www.politiaromana.ro/en/most-wanted/valug-ilie-2441970',
' https://www.politiaromana.ro/en/most-wanted/surugiu-marius-991974',
' https://www.politiaromana.ro/en/most-wanted/lupu-george-cristian-30121980',
' https://www.politiaromana.ro/en/most-wanted/grigorie-anca-hermina-1811983',
' https://www.politiaromana.ro/en/most-wanted/coman-marius-cornel-1821969',
' https://www.politiaromana.ro/en/most-wanted/capraru-calin-27101975',
' https://www.politiaromana.ro/en/most-wanted/omar-mohamad-2971971',
' https://www.politiaromana.ro/en/most-wanted/tanase-maria-8121978',
' https://www.politiaromana.ro/en/most-wanted/zamir-mordekay-2131959',
' https://www.politiaromana.ro/en/most-wanted/nanaa-ammar-121967',
' https://www.politiaromana.ro/en/most-wanted/vasi-radu-1751973',
' https://www.politiaromana.ro/en/most-wanted/pop-ioan-gheorghe-1991977',
' https://www.politiaromana.ro/en/most-wanted/bulzan-marius-dan-2791981',
' https://www.politiaromana.ro/en/most-wanted/xia-fang-1161961',
' https://www.politiaromana.ro/en/most-wanted/tarita-gheorghe-461964',
' https://www.politiaromana.ro/en/most-wanted/pandele-florentin-2671954',
' https://www.politiaromana.ro/en/most-wanted/baror-shmuel-2101949',
' https://www.politiaromana.ro/en/most-wanted/sami-youssef-fawaz-2341961',
' https://www.politiaromana.ro/en/most-wanted/boicea-lucian-2911974',
' https://www.politiaromana.ro/en/most-wanted/chita-ion-28121967',
' https://www.politiaromana.ro/en/most-wanted/zhang-lichao-2091972',
' https://www.politiaromana.ro/en/most-wanted/kumarasamy-navaneethan-831971',
' https://www.politiaromana.ro/en/most-wanted/cionca-sebastian-decebal-2181977',
' https://www.politiaromana.ro/en/most-wanted/xu-min-1951964',
' https://www.politiaromana.ro/en/most-wanted/ion-nicolaie-1071963']


for profile in allprofiles:
    driver.get(profile)
    time.sleep(1)
    
    for i in range(2,16):
        if i==4 or i==7 or i==10 or i==13:
            continue
        try:
            x = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/h3'
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/h3
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/h3
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/h3
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/h3
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/h3
            name = driver.find_element(By.XPATH,x).text 
        except NoSuchElementException:
            name = 'no Name'
        
        try:
            y = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]'
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]
            dob = driver.find_element(By.XPATH,y).text
        except NoSuchElementException:
            dob = 'no Date of Birth'
        
        try:
            z = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/span'
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/span
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/span
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/span
            place = driver.find_element(By.XPATH,z).text
        except NoSuchElementException:
            place = 'no Place of Birth'
        
        try:
            a = '//*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[2]'
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[2]
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[2]
        # //*[@id="content"]/div[2]/div[1]/div[1]/div/div[2]/p[1]
            citizenship = driver.find_element(By.XPATH, a).text
        except NoSuchElementException:
            citizenship = 'no Citizenship'
            
    print(profile + '!' + name + '!' + dob + '!'  + place + '!' + citizenship) 
    with open(r'C:\Users\Karolina.Gugudis\Desktop\Romanian Police wanted.csv', 'a', encoding="utf-8") as f: # a is for appending information to the file
        f.write(profile + '!' + name + '!' + dob + '!' + place + '!' + citizenship + '\n')
 
print('the job is done')