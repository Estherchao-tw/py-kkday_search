# /coding/python/py-kkday_klook
# -*- coding: utf-8 -*-
# python3中文轉unicode

import sys
print(sys.getdefaultencoding())
# city = input('city name')
# print(city.format(city.decode()),type(city))

a = "\u6211"
b = u"\u0432"
c = b"\u0432"
d = c.decode('utf-8')

e = "我"
f = u"我"
g = e.encode('unicode_escape')
h = e.encode('unicode_escape').decode('utf-8')

# 将中文字符串转换成 Unicode 编码


print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

print(type(e), e)
print(type(f), f)
print(type(g), g)
print(type(h), h)
