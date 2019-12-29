import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome("D:\All Software\Different Software\chromedriver")
driver.get('https://www.facebook.com/')
driver.find_element_by_name('firstname').send_keys('Shahjahan')
driver.find_element_by_name('lastname').send_keys('Kabir')
driver.find_element_by_id('u_0_r').send_keys('01746484619')
driver.find_element_by_id('u_0_w').send_keys('25802580')

drp_date = driver.find_element_by_id('day')
select_date = Select(drp_date)
select_date.select_by_visible_text('10')

drp_month = driver.find_element_by_id('month')
select_month = Select(drp_month)
select_month.select_by_index(11)
print(len(select_month.options))
for month in select_month.options:
   print(month.text)

drp_year = driver.find_element_by_id('year')
select_year = Select(drp_year)
select_year.select_by_visible_text('1994')
time.sleep(5)
try:
    driver.find_element_by_id('u_0_a').click()

except:
    pass
driver.find_element_by_name('websubmit').click()