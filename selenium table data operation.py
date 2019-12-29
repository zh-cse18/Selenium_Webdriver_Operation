from selenium import webdriver

driver = webdriver.Chrome("D:\All Software\Different Software\chromedriver")
driver.get("file:///C:/Users/PC/Desktop/Camera/sample table.html")
rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols =len(driver.find_elements_by_xpath('/html/body/table/tbody/tr[1]/th'))

print(rows,cols)
for row in range(2, rows+1):
    for col in range(1, cols +1):
       print( driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(row)+"]/td["+str(col)+"]").text,end="   ")
    print('\n')
