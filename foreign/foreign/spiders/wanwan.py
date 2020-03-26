# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-18 16:40 '

# from selenium import webdriver
# brower = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# brower.get('https://www.baidu.com')
# print(brower.page_source)
from pyquery import PyQuery as pq
doc = pq(filename='demo.html')
print(doc(''))