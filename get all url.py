from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome("E:\All Software\Different Software\chromedriver")
driver.get("https://www.google.com/search?q=how+to+get+a+url+using+selenium&rlz=1C1GCEA_enBD872BD872&oq=how+to+get+a+url+using+se&aqs=chrome.5.69i57j33l5.24591j0j7&sourceid=chrome&ie=UTF-8")
ids = driver.find_elements_by_xpath("//*[@href]")
for id in ids:
    print(id.get_attribute('href'))
driver.quit()
