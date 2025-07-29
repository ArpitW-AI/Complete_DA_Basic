from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service("E:/arpit/study/python/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

# opening google page
driver.get('http:duckduckgo.com')
time.sleep(2)

# giving input 'smartprix'
user=driver.find_element(by=By.XPATH, value='//*[@id="searchbox_input"]')
user.send_keys("smartprix")
time.sleep(2)
user.send_keys(Keys.ENTER)
time.sleep(2)

# reaching the site
c1=driver.find_element(by=By.XPATH, value='//*[@id="r1-0"]/div[3]/h2/a/span')
c1.click()
time.sleep(3)

# clicking mobile option
c2=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[3]/div/a[4]/img')
c2.click()
time.sleep(3)

# sorting category
c3=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
c3.click()
time.sleep(3)

c4=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
c4.click()
time.sleep(3)

c5=driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[17]/div[2]/label[1]/input')
c5.click()
time.sleep(3)

# scrolling to end
old_height=driver.execute_script('return document.body.scrollHeight')
c=0
while True:
    driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(2)
    new_height=driver.execute_script('return document.body.scrollHeight')
    print(c)
    print(old_height)
    print(new_height)

    if (new_height == old_height) or (c==41):
        break

    old_height=new_height
    c+=1


# html=driver.page_source
# with open('smartprix.html','w', encoding='utf-8')as f:
#     f.write(html)



input("Press Enter To exit...")