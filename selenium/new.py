from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service("E:/arpit/study/python/chromedriver-win64/chromedriver.exe")

driver= webdriver.Chrome(service=s)
driver.get("http://google.com")
time.sleep(5)

user_input=driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('campusx')
time.sleep(5)

user_input.send_keys(Keys.ENTER)
time.sleep(6)


input("Press Enter to exit...")