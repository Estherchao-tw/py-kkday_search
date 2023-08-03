# -*- coding: utf-8 -*-
"""
@File  : kkday-scrapy_class.py
@Author: EstherChao
@Date  : 2023/8/3 12:15
@Desc  : 爬蟲
"""
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Kkday:
    #建構式
    def __init__(self,city_name):
        self.city_name = city_name #城市屬性

    #方法:爬蟲主程式
    def scrape(self):
        
        #使用selenium连接网络
        def selenium_chrome(url):
            option = Options()
            #使用無痕模式
            option.add_argument("--incognito")
            # 打開chrome網頁
            browser = webdriver.Chrome(options=option)
            browser.get(url)

            return browser


        # 如果city_name 不是空的
        if self.city_name: 
            result = [] #回傳資料#收集data
            url = "https://www.kkday.com/zh-tw/product/productlist?page=1&city={}&cat=TAG_4_4&sort=prec".format(self.city_name)
            browser = selenium_chrome(url)

            soup = BeautifulSoup(browser.page_source, 'html.parser',on_duplicate_attribute='ignore')
            # 取得資料dict
            data = soup.find_all('div',{'class':"product-listview search-info gtm-prod-card-element"})

            # 爬取想要的資料
            #　標題、連結、價格、可使用日期、評分
            for detail in data:
                title = detail.find('span',{'class':"product-listview__name"}).text
                date = detail.find('div',{'class':"product-time-icon"}).text.replace('\t','').replace('\n','')
                price = detail.find('div',{'class':"product-pricing"}).text.replace('\t','').replace('\n','')
                star = detail.find('div',{'class':"product-star"}).text.replace('(','').replace(')','')
                link= detail.find('a').get('href')

                result.append(dict(title=title,date=date,price=price,star=star,link=link))
                
            print("success")
            return result
        time.sleep(5)
        browser.close(); #closes the browser


            

print("start...") 
demo = Kkday("A01-001-00010") 
print(demo.scrape())  
