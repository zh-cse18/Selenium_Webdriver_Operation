from selenium import webdriver

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

links =driver.find_elements_by_tag_name('a')
# links =driver.find_element_by_attribute('href')

for link in links:
    print(link.text)
    print(link.get_attribute('href'))
