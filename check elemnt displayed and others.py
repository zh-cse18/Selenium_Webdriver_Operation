import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

# Setup the ChromeDriver with webdriver-manager
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

username = driver.find_element_by_name('userName')
print(username.is_displayed(), username.is_enabled())
if(username.is_displayed() and username.is_enabled()):
    username.send_keys('zahid')

password = driver.find_element_by_name('password')
print(password.is_displayed(),password.is_enabled())
if(password.is_displayed(),password.is_enabled()):
    password.send_keys('passwordunknown')

login = driver.find_element_by_name('login')
login.click()

round_trip_radio_button = driver.find_element_by_css_selector("input[value = roundtrip]").is_selected()
driver.find_element_by_css_selector("input[value = oneway]").click()



