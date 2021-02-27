import time

import pyautogui as pyautogui
from selenium import webdriver

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("https://evaly.com.bd/")
time.sleep(30)
print("waiting time end")
cancel_btn = driver.find_element_by_xpath('/html/body/reach-portal[1]/div/div/div/section/div/button')
print(cancel_btn)
cancel_btn.click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/div/div/input').send_keys("Asus Laptop")
pyautogui.press('enter')
#driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[2]/div[1]/div/div[2]/form/div/input').click()
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath('//*[@id="__next"]/div/div/div[3]/div/div[2]/div[2]/ul/li[13]/a/a/div/div[1]/div/img')