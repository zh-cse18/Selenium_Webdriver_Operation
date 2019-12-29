from selenium import webdriver

driver = webdriver.Chrome("D:\All Software\Different Software\chromedriver")
driver.get('https://www.facebook.com/')
driver.find_element_by_name('email').send_keys('01766022841')
driver.find_element_by_name('pass').send_keys('Bangladesh')
driver.find_element_by_id('loginbutton').click()
