# -*- coding: utf-8 -*-
"""
@File  : kkday-scrapy.py
@Author: EstherChao
@Date  : 2023/7/31 17:15
@Desc  : 爬蟲
"""

from bs4 import BeautifulSoup
import random
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#使用selenium连接网络
def selenium_chrome(url):
    option = Options()
    #使用無痕模式
    option.add_argument("--incognito")
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser = webdriver.Chrome(options=option)
    browser.get(url)

    return browser


# 儲存資料
def write_data_json(all_scripts):
    for script in all_scripts:
        if 'affiliate_pay_report_orderName' in script.text:
            with open('script2.json','w',encoding='utf-8') as file :
                json.dump(script.text,file)


if __name__ == '__main__':
    result = [] #收集data
    print("start...")    
    city_name = "A01-001-00013"
    url = "https://www.kkday.com/zh-tw/product/productlist?page=1&city={}&cat=TAG_4_4&sort=prec".format(city_name)
    browser = selenium_chrome(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    all_scripts = soup.find_all("script")

    time.sleep(5)
    write_data_json(all_scripts)
    browser.close()