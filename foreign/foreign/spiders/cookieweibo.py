# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-03-18 16:40 '
import urllib
import urllib2
import time
import requests
import re

import sys
import os
import string

'''
编码方式的设置,在中文使用时用到中文时的处理方式
'''
default_encoding = "utf-8"
if sys.getdefaultencoding() != default_encoding:
  reload(sys)
  sys.setdefaultencoding("utf-8")
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0',
	'Cookie':"_T_WM=31de080566a1a9928fd816f277f014c7; SUB=_2A25zda8zDeRhGeFM4lIW-SvEyD-IHXVQmTF7rDV6PUJbkdAKLUb-kW1NQIuqBRJnBT2nr005EZ12YlzOsqnUGpUJ; SUHB=0jBICa8zSCF_j7; SCF=Am-qtQI_KiIre1hIiaUOdQXnjreu48ye1z6jyYAufhJ7qlqHawQQ17R06SeS6w3RGMEAor0tOQIhzWpwEPQnfcc.; SSOLoginState=1584521059",
    # 'cookie':'WEIBOCN_FROM=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; path=/; domain=.weibo.cn',
	'Referer':"https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn&st=ef5d80&id=&_T_WM=31de080566a1a9928fd816f277f014c7"
}
post_url='https://weibo.cn/mblog/sendmblog?st=ee5369'
content = 'hahha测试'
post_data={'rl':'0','content':content}
r=requests.post(post_url,headers=headers,verify=False)
r.encoding = 'utf-8'
print r.text
if(r.status_code==200):#....不对
	print "发送微博成功"
else:
	print "微博发送失败,请检查cookies是否过期"