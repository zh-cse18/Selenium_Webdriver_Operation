from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("http://coredogs.com/lesson/web-page-tables.html")

rows = len(driver.find_elements_by_xpath('//tbody/tr'))
cols = len(driver.find_elements_by_xpath('//tbody/tr[1]/th'))
print(rows, cols)

for i in range(2, 5):
    for c in range(1, 4):
        print(str(i), str(c))
        coleelement = driver.find_element_by_xpath('//*[@id="node-356"]/div[2]/table/tbody/tr["str(i)"]/td["str(c)"]')
        #coleelement = driver.find_element_by_xpath('//tbody/tr["str(i)"]/td["str(c)"]').text
        print(coleelement.text)
driver.quit()
