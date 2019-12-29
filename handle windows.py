from selenium import webdriver

driver = webdriver.Chrome("D:\All Software\Different Software\chromedriver")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
handles = driver.window_handles
for window in handles:
    driver.switch_to_window(window)
    print(driver.title)
driver.quite()
