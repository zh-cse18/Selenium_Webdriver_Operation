import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.get("http://www.expedia.com/")
driver.maximize_window()
driver.find_element(By.ID,"tab-flight-tab-hp").click()
driver.find_element_by_id("flight-origin-hp-flight").send_keys('SFO')
driver.find_element_by_id("flight-destination-hp-flight").send_keys('NYC')

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys('2/26/2021')

driver.find_element_by_id("flight-returning-hp-flight").clear()
# driver.find_element_by_id("flight-returning-hp-flight").send_keys('12/31/2019')

driver.find_element_by_name("endDate").send_keys('2/28/2021')
driver.find_element_by_id("flight-returning-hp-flight").click()

wait = WebDriverWait(driver,5)
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id ='stopFilter_stops-0']")))

# driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/lebel/button").click()
