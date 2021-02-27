from selenium import webdriver

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
driver.close()