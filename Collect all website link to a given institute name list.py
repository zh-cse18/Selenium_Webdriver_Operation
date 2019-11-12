from threading import Thread
from time import sleep
import csv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
# with open('urls.txt', 'r') as fobj:
#     hospitals = fobj.readlines()
hospitals = [
"GRANT MEMORIAL HOSPITAL" ,
"BROADDUS HOSPITAL ASSOCIATION, INC" ,
"PLEASANT VALLEY HOSPITAL" ,
"PRINCETON COMMUNITY HOSPITAL" ,
"JEFFERSON MEDICAL CENTER" ,
"JACKSON GENERAL HOSPITAL" ,
"HAMPSHIRE MEMORIAL HOSPITAL" ,
"GREENBRIER VALLEY MEDICAL CENTER" ,
"SISTERSVILLE GENERAL HOSPITAL" ,
"THOMAS MEMORIAL HOSPITAL" ,
"ROANE GENERAL HOSPITAL" ,
"SUMMERSVILLE REGIONAL MEDICAL CENTER" ,
"WEBSTER COUNTY MEMORIAL HOSPITAL" ,
"WEIRTON MEDICAL CENTER" ,
"WELCH COMMUNITY HOSPITAL" ,
"STONEWALL JACKSON MEMORIAL HOSPITAL" ,
"OHIO VALLEY MEDICAL CENTER" ,
"WHEELING HOSPITAL" ,
"WILLIAMSON MEMORIAL HOSPITAL" ,
"STAR VALLEY MEDICAL CENTER" ,
"SOUTH BIG HORN COUNTY CRITICAL ACCESS HOSPITAL" ,
"JOHNSON COUNTY HEALTHCARE CENTER" ,
"MOUNTAIN VIEW REGIONAL HOSPITAL" ,
"SUMMIT MEDICAL CENTER" ,
"WYOMING MEDICAL CENTER" ,
"CHEYENNE REGIONAL MEDICAL CENTER" ,
"WEST PARK HOSPITAL DISTRICT" ,
"MEMORIAL HOSPITAL OF CONVERSE COUNTY" ,
"EVANSTON REGIONAL HOSPITAL" ,
"CAMPBELL COUNTY MEMORIAL HOSPITAL" ,
"ST JOHNS MEDICAL CENTER" ,
"SOUTH LINCOLN MEDICAL CENTER - CAH" ,
"IVINSON MEMORIAL HOSPITAL" ,
"NORTH BIG HORN HOSPITAL DISTRICT" ,
"NIOBRARA HEALTH & LIFE CENTER" ,
"WESTON COUNTY HEALTH SERVICES" ,
"POWELL VALLEY HOSPITAL" ,
"MEMORIAL HOSPITAL OF CARBON COUNTY" ,
"SAGEWEST HEALTH CARE" ,
"MEMORIAL HOSPITAL SWEETWATER COUNTY" ,
"SHERIDAN MEMORIAL HOSPITAL" ,
"CROOK COUNTY HOSPITAL" ,
"HOT SPRINGS COUNTY MEMORIAL HOSPITAL" ,
"COMMUNITY HOSPITAL" ,
"PLATTE COUNTY MEMORIAL HOSPITAL" ,
"WASHAKIE MEDICAL CENTER"]
count =1

for search_String in hospitals:
    driver = webdriver.Chrome("E:\All Software\Different Software\chromedriver")
    # driver.set_window_position(400,100)
    # driver.get("https://www.google.com")
    driver.get('https://www.bing.com/')
    # driver.find_element_by_xpath("//input[@name='q']").send_keys('ALASKA NATIVE MEDICAL CENTER')
    # search_String ="ALASKA NATIVE MEDICAL CENTER"
    get_input_field = driver.find_element_by_name("q")
    try:
        get_input_field.send_keys(search_String)
        get_input_field.send_keys(Keys.ENTER)
        sleep(1)
        info = driver.find_element_by_partial_link_text(search_String.title())
        print(str(count) + ".  " + search_String + "---------------" + info.get_attribute('href'))
        list_items = [[search_String, info.get_attribute('href')]]

        with open('Result.csv', 'a') as wcsv:
            fcsv = csv.writer(wcsv)
            fcsv.writerows(list_items)
            count +=1
        driver.close()
    except:
        driver.close()

driver.quit()