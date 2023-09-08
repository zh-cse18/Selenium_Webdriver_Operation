import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

# Setup the ChromeDriver with webdriver-manager
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

# Navigate to Google.com and perform a search
driver.get("http://newtours.demoaut.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('Python automation with Selenium')
search_box.submit()

# Assert that the search query is present in the resulting page title
# assert 'Python automation with Selenium' in driver.title

# Quit the driver
driver.quit()
driver.close()

