from selenium import webdriver


driver = webdriver.Chrome("D:\All Software\Different Software\chromedriver")
driver.get("http://www.w3school.com")
driver.execute_script("window.scrollBy(0,10000)", " ") # scroll a fixed postition

#scroll down till a element is visiable
# flag = driver.find_element_by_xpath('//*[@id="mainContent"]/div/div[3]/p[178]/a')
# driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("http://www.w3school.com")

# driver.execute_script("window.scrollBy(0,5000)", " ") # scroll a fixed postition

#scroll down till a element is visiable
flag = driver.find_element_by_xpath('//body/div[1]/div[4]/p[7]/img[1]')
driver.execute_script("arguments[0].scrollIntoView();", flag)

#scroll till end
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

