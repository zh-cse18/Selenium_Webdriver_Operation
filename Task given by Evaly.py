import time

import flag as flag
import pyautogui as pyautogui
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("F:\Development\chromedriver\chromedriver")
driver.maximize_window()
# open evaly site
driver.get("https://beta.evaly.com.bd/")

# cancel pop up screen
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[@class="absolute top-0 right-0 p-2"]'))

    )
    element.click()
finally:
    pass
time.sleep(5)

# Login start
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/span[1]"))
    )
    element.click()
finally:
    pass

time.sleep(5)


def login(phone_xpath, cell_no, pass_xpath, password):
    driver.find_element_by_xpath(phone_xpath).send_keys(cell_no)
    driver.find_element_by_xpath(pass_xpath).send_keys(password)
    pyautogui.press('enter')


# login completed
login('//input[@name="phone"]', '01681442238', '//input[@name="password"]', 'musa1990#')


#  method for cancel after buy cart screen
def cancelRightSidebar():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='mr-4 align-middle']"))
        )
        element.click()
    finally:
        pass


time.sleep(10)

# click on all shop
driver.find_element_by_xpath("//a[contains(text(),'All Shops')]").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@placeholder='Search...']").send_keys('Test Shop Joker')
pyautogui.press('enter')
# time.sleep(5)

# click on Test Shop Jokar  Shop
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(),'Test Shop Joker')]"))
    )
    element.click()
finally:
    pass

# add  a item in cart
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/div[3]/div/div[4]/div[3]/div[2]/div[3]/div[4]/button"))
    )
    element.click()
finally:
    pass
# sleep browser for 5 seconds
time.sleep(5)
cancelRightSidebar()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/div[3]/div/div[4]/div[3]/div[2]/div[3]/div[4]/button"))
    )
    element.click()
finally:
    pass
# sleep browser for 5 seconds

time.sleep(5)

#  method for cancel after buy cart screen
def cancelRightSidebar():
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@class='mr-4 align-middle']"))
        )
        element.click()
    finally:
        pass


cancelRightSidebar()

# sleep browser for 5 seconds
time.sleep(5)


#add  another item in cart
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/div[3]/div/div[4]/div[3]/div[2]/div[5]/div[4]/button"))
    )
    element.click()
finally:
    pass
time.sleep(5)

# cancel after buy now right side bar.
cancelRightSidebar()
# click on show already  added in cart item
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[@class='Cart___StyledSpan-sc-38u3yk-1 fxlzgQ']"))
    )
    element.click()
finally:
     pass

# #delete a item from cart
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/ul/li[2]/div/button"))
    )
    element.click()
finally:
    pass
time.sleep(5)

# click on proceed to check out
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(),'Proceed to checkout')]"))
    )
    element.click()
finally:
    pass

# click on confirm order
time.sleep(5)
driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/button[1]").click()

# click on accept terms and conditions check box.
time.sleep(5)
driver.find_element_by_xpath("//input[@type='checkbox']").click()

# click on final confirm order
time.sleep(5)
driver.find_element_by_xpath("//*[@id='__next']/div/div[3]/div/div/div[1]/div/div[3]/div[2]/div[2]/button").click()
time.sleep(5)
# scroll top to bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# click on SSl Payment
time.sleep(5)
driver.find_element_by_xpath("//*[@id='__next']/div/div/ul/li[8]/div[2]").click()

# click on Success from ssl page
time.sleep(5)
driver.find_element_by_xpath("//input[@value='Success']").click()

# click on payment method VISA
time.sleep(5)
driver.find_element_by_xpath("//img[@src='https://sandbox.sslcommerz.com/gwprocess/v4/assets/img/visa-sq.png']").click()

# click on final payment success
time.sleep(5)
driver.find_element_by_xpath("//button[@type='submit']").click()
# driver.quite()
