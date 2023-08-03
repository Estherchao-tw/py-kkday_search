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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def get_user_agent():
#     user_agent_list=[
#         # chrome
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
#         "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"
#     ]
#     UserAgent = random.choice(user_agent_list)
#     return UserAgent

#使用selenium连接网络
def selenium_chrome(url):
    option = Options()
    #使用無痕模式
    option.add_argument("--incognito")
    
    # ua = get_user_agent()
    # option.add_argument("user-agent={}".format(ua))
    browser = webdriver.Chrome(options=option)
    browser.get(url)

    return browser

if __name__ == '__main__':
    result = [] #收集data
    print("start...")    
    city_name = "A01-001-00009"
    page=1
    url = "https://www.kkday.com/zh-tw/product/productlist?page=1&city={}&cat=TAG_4_4&sort=prec".format(city_name)
    browser = selenium_chrome(url)

    soup = BeautifulSoup(browser.page_source, 'html.parser',on_duplicate_attribute='ignore')
    # 取得資料dict
    data = soup.find_all('div',{'class':"product-listview search-info gtm-prod-card-element"})
    # print(data)
    # 爬取想要的資料
    #　標題、連結、價格、可使用日期、評分
    for detail in data:
        title = detail.find('span',{'class':"product-listview__name"}).text
        date = detail.find('div',{'class':"product-time-icon"}).text.replace('\t','').replace('\n','')
        price = detail.find('div',{'class':"product-pricing"}).text.replace('\t','').replace('\n','')
        star = detail.find('div',{'class':"product-star"}).text.replace('(','').replace(')','')
        link= detail.find('a').get('href')

        # print(type(title))
        # print(date.text.strip())
        # print(price.text.strip())
        # print(star.text)
        # print(link)
        result.append(dict(title=title,date=date,price=price,star=star,link=link))
        
    print(result,"success")

    time.sleep(5)
