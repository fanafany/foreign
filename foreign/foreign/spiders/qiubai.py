import requests
from lxml import etree
import json


def index_spider(n):
    url = 'http://health.people.com.cn/GB/408575/index{0}.html'.format(n)
    print('当前',url)
    header = {
        'Host':'health.people.com.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    response = requests.get(url,header)
    response.encoding = "gb2312"
    html = etree.HTML(response.text)
    urls = html.xpath('//div[@class="newsItems"]/a/@href')
    keyword = html.xpath('//div[@class="subNav"]/a[3]/text()')
    keywords = ''.join(keyword)
    dics = []
    s = 0
    lens = len(urls)
    for i in urls:
        item = 'http://health.people.com.cn'+i
        print(item)
        try:
            res = requests.get(item,header)
            res.encoding = 'gb2312'
            htmls = etree.HTML(res.text)
            title = htmls.xpath("//div[@class='title']/h2/text()")
            titles = ''.join(title)
            content = htmls.xpath("//div[@class='artOri']/text()".replace('来源：',''))
            conts = ''.join(content).replace("来源：","")
            contents = htmls.xpath("//div[@class='artDet']/p/text()")
            contems = ''.join(contents)
            sutit = html.xpath("//div[@class='artDet']/p[position()>0 and position()<3]/text()")
            subtitle = ''.join(sutit)
            s += 1
            dic = {

                "title":titles,
                'time':conts,
                'fcount':item,
                'keywords':keywords,
                'subtitle':subtitle,
                'content':contems
            }
            dics.append(dic)
        except:
            pass
    print('正在输出第',n)
    lens += lens
    print(lens)
    return dics

if __name__ == '__main__':
    # print(dic)
    for i in range(1,2):
        text = index_spider(i)
        print(text)
        # print('-------------------------------------')
        # print('-------------------------------------')
        # with open('data3.json','a',encoding='utf-8')as file:
        #     file.write(json.dumps(text,indent=2, ensure_ascii=False))

