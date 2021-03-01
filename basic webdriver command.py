from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.get("https://evaly.com.bd/")
time.sleep(5)
print(driver.title)
time.sleep(5)
driver.get("https://facebook.com/")
print(driver.title)
time.sleep(5)
driver.back()
driver.back()

time.sleep(5)
driver.forward()
time.sleep(5)
driver.forward()
time.sleep(5)