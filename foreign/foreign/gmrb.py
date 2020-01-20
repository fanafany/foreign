# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-16 17:02 '
import requests
from lxml import etree


class Gmrb():
    def __init__(self):
        self.url = 'https://epaper.gmw.cn/gmrb/html/2008-01/01/nbs.D110000gmrb_01.htm'
        self.header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        }


    def datime(self):
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
        offset = str(offset.strftime('%Y-%m/%d'))

        return offset

    def parse(self,url):
        sou = 'https://epaper.gmw.cn/gmrb/'
        req = requests.get(self.url, headers=self.header).text
        html = etree.HTML(req)
        title = html.xpath("//div[@id='pageList']/ul/li/a[2]/@href")
        text = html.xpath("//div[@id='pageList']/ul/li/a/text()")
        for i in title:
            titles = ''.join(i).replace('../', '')
            tit = sou + titles

while True:
    offset = Gmrb.datime('1')

    while str(offset.strftime('%Y-%m-%d')) != endnow:
        offset += delta
        print(offset)
    print('test'*5)


