from selenium import webdriver

driver = webdriver.Chrome("D:\All Software\Different Software\chromedriver")
driver.get("http://newtours.demoaut.com/")
print( '1st site :',driver.title)
driver.get("http://google.com/")
print('2nd site',driver.title)
driver.back()
print('after back 1st site :',driver.title)
driver.forward()
print('after forward 2nd site: ',driver.title)
print(driver.title)
