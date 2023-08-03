# -*- coding: utf-8 -*-
"""
@File  : kkdaytest.py
@Author: EstherChao
@Date  : 2023/7/31 17:15
@Desc  : 爬蟲
"""
from bs4 import BeautifulSoup
import random
import time
import json
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#使用selenium连接网络
def selenium_chrome(url):
    option = Options()
    #使用無痕模式
    option.add_argument("--incognito")
    #解決 error certificate Error parsing cert retrieved from AIA (as DER):
    # ERROR: Couldn't read tbsCertificate as SEQUENCE
    # ERROR: Failed parsing Certificate
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    #不打開視窗繼續執行
    # option.add_argument("headless")
    # 打開chrome網頁
    browser = webdriver.Chrome(options=option)
    browser.get(url)

    return browser

# 中文轉成unicode
def c_to_unicode(city_name):
    # city_name type is str
    # 内容是str，但是需要轉化type變成是unicode,就可以使用 encode('unicode_escape')
    # 轉成unicode 會有b的前綴符號，要去掉就可以使用 decode('utf-8)
    to_unicode = city_name.encode('unicode_escape').decode('utf-8')
    return to_unicode



# unicode 比較 script的data中是否符合
# all script 的類型是<class 'bs4.element.ResultSet'>
## 透過for loop 將script(line)儲存成 <class 'str'>
# 並將unicode 後的 cityname 放入判斷是否在script裡面
def compare_city_name(uni_city_name):
    with open("./script1.json") as all_script:
        data = json.load(all_script)
        # print(data)
        print(uni_city_name)
        
        #判斷cityname
        for line in data:
            if line.find(uni_city_name) != -1:
                print(line.find(uni_city_name))
                return uni_city_name 
                    # print(line.text)
            else:
                print("error,it's a wrong city name")
                print(uni_city_name)
                return False

if __name__ == '__main__':
    print("start...")
    city_name = "A01-001-00001"
    page=1
    url = "https://www.kkday.com/zh-tw/product/productlist?page=1&city={}&cat=TAG_4_4&sort=prec".format(city_name)
    browser = selenium_chrome(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser',on_duplicate_attribute='ignore')
    all_scripts = soup.find_all("script")

    time.sleep(5)
    browser.close()
    a = input("city_name") 
    b = c_to_unicode(a) # \u65b0\u7af9 <class 'str'>
    print(b)
    compare_city_name(b)
    print(compare_city_name(b))

    # write_data_json(all_scripts)
