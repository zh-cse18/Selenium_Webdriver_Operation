# import csv
# from parsel import Selector
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# hospitals = ['ALASKA NATIVE MEDICAL CENTER', 'ALASKA REGIONAL HOSPITAL']
# # x = 'ALASKA REGIONAL HOSPITAL'
# for u in hospitals:
#     driver = webdriver.Chrome("E:\All Software\Different Software\chromedriver")
#     driver.get('https://www.bing.com/')
#     # for x in  (range(hospitals)):
#     search_query = driver.find_element_by_name('q')
#     search_query.send_keys(u)
#     sleep(0.5)
#     search_query.send_keys(Keys.ENTER)
#     sleep(1)
#     sel = Selector(text=driver.page_source)
#     results = sel.xpath("//h2[@class='b_topTitle']/a/@href").extract_first()
#     print(results)
#     sleep(1)
#
#     # driver.quit()
#     # driver.close()
#


import csv
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('urls.txt', 'r') as fobj:
    hospitals = fobj.readlines()

for x in hospitals:
    driver = webdriver.Chrome("E:\All Software\Different Software\chromedriver")
    driver.get('https://www.bing.com/')
    search_query = driver.find_element_by_name('q')
    search_query.send_keys(x)
    sleep(5)
    search_query.send_keys(Keys.ENTER)
    sleep(0.5)

    sel = Selector(text=driver.page_source)
    # results = driver.find_element_by_tag_name("cite")
    # results = results.text
    results = sel.xpath("//div[@class='b_attribution']/cite[1]/text()").extract_first()
    with open('url.txt', 'a', encoding='UTF-8') as fobj:
        fobj.write('\n' + str(results))
    print(results)
    sleep(1)
    driver.close()
