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
#Login start
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/span[1]"))
    )
    element.click()
finally:
    pass

time.sleep(5)
driver.find_element_by_xpath('//input[@name="phone"]').send_keys('01746484619')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('100barloveu#')
pyautogui.press('enter')
#login completed
time.sleep(10)

#click all shop
driver.find_element_by_xpath("//a[contains(text(),'All Shops')]").click()
time.sleep(5)

#click on Evaly Hero Official Store
driver.find_element_by_xpath("//p[contains(text(),'Evaly Hero Official Store')]").click()

#click on buy now button
driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[3]/div[1]/div[3]/div[3]/div[2]/div[1]/div[4]/button[1]").click()
