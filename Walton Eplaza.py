import time
import pyautogui as pyautogui
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("https://waltonbd.com/")
# driver.find_element_by_xpath("//a[contains(text(),'About Us')]")
driver.execute_script("window.scrollTo(5,document.body.scrollHeight)")
time.sleep(3)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'E-Plaza')]"))
        # EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "E-PLAZA"))

    )
    element.click()
finally:
    pass

