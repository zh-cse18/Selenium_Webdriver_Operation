
from appium import webdriver
desired_cap = {
    "platformName": "Android",
    "deviceName": "Android",
    #"app": "D:/Different Apk/chaldal.apk",
    #"appPackage": "com.chaldal.poached",
    "appPackage": "com.android.camera",
    #"appActivity": "com.chaldal.poached.MainActivity",
    "appActivity": "com.android.camera.Camera"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
#driver.find_element_by_id("v9_shutter_button_internal").click()
for i in range(10):
    driver.find_element_by_id("v9_shutter_button_internal").click()
    print(i)
