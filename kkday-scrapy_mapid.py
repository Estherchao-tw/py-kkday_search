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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def get_useragent():
    user_agent_list=[
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"
    ]
    UserAgent = random.choice(user_agent_list)

#使用selenium连接网络
def selenium_chrome(url):
    option = Options()
    #使用無痕模式
    option.add_argument("--incognito")
    
    ua = get_useragent()
    option.add_argument("user-agent={}".format(ua))
    browser = webdriver.Chrome(options=option)
    browser.get(url)

    return browser

# 中文轉成unicode
def c_to_unicode(city_name):
    to_unicode = city_name.encode('unicode_escape').decode('utf-8')

    # print(to_unicode)
    # print(to_unicode,type(to_unicode))
    return to_unicode
# 在script中找到data
def script_tran(all_script):
    for script in all_script:
        if '{"select_country"' in script.text:
            # print(number,paragraphs)
             print(type(script.text))
             print(script.text)

    return script.text

# unicode 比較 script中是否符合
def compare_city_name(b,all_scripts):
        
    for line in all_scripts:

        if line.find(b) != -1:
            print(b,line.find(b) != -1)
            # print(line.text)
        else:
            print("error,it's a wrong city name")
    return b

if __name__ == '__main__':
    print("start...")
    city_name = "A01-001-00010"
    page=1
    url = "https://www.kkday.com/zh-tw/product/productlist?page=1&city={}&cat=TAG_4_4&sort=prec".format(city_name)
    browser = selenium_chrome(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    all_scripts = soup.find_all("script")


    print(type(all_scripts))
    script0 = script_tran(all_scripts)
    
    print(type(script0))

        

    time.sleep(2)


    a = input("city_name")
    b = c_to_unicode(a)
    print(b,type(b))
    compare_city_name(b,all_scripts)
