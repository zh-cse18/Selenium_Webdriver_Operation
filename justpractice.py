from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

# 0 - Default, 1 - Allow, 2 - Block
chrome_options = Options()
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 1})
desired_cap = chrome_options.to_capabilities()
desired_cap.update({
  'browser_version': '88.0',
  'os': 'Windows',
  'os_version': '10'
})
driver = webdriver.Remote(command_executor='http://YOUR_USERNAME:YOUR_ACCESS_KEY@hub.browserstack.com/wd/hub', desired_capabilities=desired_cap)
driver.get("https://web-push-book.gauntface.com/demos/notification-examples/")
driver.find_element_by_xpath("//body/main[1]/p[3]/input[1]").click()
time.sleep(2)
driver.quit()