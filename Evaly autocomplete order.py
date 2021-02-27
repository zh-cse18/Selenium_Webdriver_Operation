import time

import pyautogui as pyautogui
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("https://evaly.com.bd/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/reach-portal[1]/div/div/div/section/div/button"))

    )
    element.click()
finally:
    pass
time.sleep(30)
# print("waiting time end")
# cancel_btn = driver.find_element_by_xpath('/html/body/reach-portal[1]/div/div/div/section/div/button')
# print(cancel_btn)
# cancel_btn.click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/div/div/input').send_keys("Asus Laptop")
pyautogui.press('enter')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[3]/div/div[2]/div[2]/ul/li[13]/a/a/div/div[1]/div/img'))
    )
    element.click()
finally:
    pass
#
#
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[2]/div/button/span/span/svg'))
#     )
#     element.click()
# finally:
#     pass

