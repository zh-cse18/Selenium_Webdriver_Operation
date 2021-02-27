import time
from selenium import webdriver
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H")

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.get('https://www.facebook.com/')

if int(current_time) <= 14:
    driver.find_element_by_name('email').send_keys('01766022841')
    driver.find_element_by_name('pass').send_keys('Bangladesh')

    driver.find_element_by_name('login').click()
while True:
    time.sleep(10)
    driver.refresh()
