
from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("D:\Automation software\Chromedriver88\chromedriver")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element = driver.find_element_by_id('RESULT_RadioButton-9')
drp =Select(element)
# select by index
drp.select_by_index(2)

# select by  value
drp.select_by_value("Radio-2")

# select by visiable text
drp.select_by_visible_text("Morning")

