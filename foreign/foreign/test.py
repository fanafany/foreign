# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-16 10:52 '

import requests
from lxml import etree
import urllib.request
import os
import codecs
import urllib


def geturl(url):
    from datetime import datetime
    datime = '2008-01/01'
    now = datetime.strptime(datime, "%Y-%m/%d")
    # 递增的时间
    import datetime
    delta = datetime.timedelta(days=1)
    # 六天后的时间
    endnow = now + datetime.timedelta(days=50)
    # 六天后的时间转换成字符串
    endnow = str(endnow.strftime('%Y-%m/%d'))
    offset = now
    offset += delta

    while str(offset.strftime('%Y-%m/%d')) != endnow:
        offset += delta
        sous = str(offset.strftime('%Y-%m/%d'))

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    sou = 'https://epaper.gmw.cn/gmrb/'
    req = requests.get(url,headers = header).text
    html = etree.HTML(req)
    title = html.xpath("//div[@id='pageList']/ul/li/a[2]/@href")
    text = html.xpath("//div[@id='pageList']/ul/li/a/text()")
    for e in text:
        texts = e
    for s in title:
        titles = ''.join(s).replace('../', '')
        tit = sou + titles
        file = urllib.request.urlopen(tit)

    with open(str(texts)+'.pdf', 'wb')as fp:
        fp.write(file.read())

    return tit

while True:

    geturl(url = 'https://epaper.gmw.cn/gmrb/html/{}/nbs.D110000gmrb_01.htm'.format(sous))
# def getFile(url):
#     file = urllib.request.urlopen(url)
#     # f = codecs.open(r'D:\foreign\foreign\foreign\images'+'1.pdf','wb')
#
#     with open('.pdf','wb')as fp:
#         fp.write(file.read())
#
#
# getFile(tit)





