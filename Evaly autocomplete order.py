import time
import pyautogui as pyautogui
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
# open evaly site
driver.get("https://evaly.com.bd/")

# cancel pop up screen
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="absolute top-0 right-0 p-2 text-white"]'))

    )
    element.click()
finally:
    pass


time.sleep(5)
# write Asus Laptop in search box
driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/div/div/input').send_keys("Asus Laptop")
# Press enter button
pyautogui.press('enter')


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="__next"]/div/div/div[3]/div/div[2]/div[2]/ul/li[13]/a/a/div/div[1]/div/img'))
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
