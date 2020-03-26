# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-16 10:52 '
import requests
from lxml import etree
url = 'http://health.people.com.cn/n1/2020/0326/c14739-31649002.html'
header = {
        'Host':'health.people.com.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
resp = requests.get(url,headers=header).text
html = etree.HTML(resp)


