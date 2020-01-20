# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-08 15:12 '


# from datetime import datetime
# from datetime import timedelta
# datime = '2008-01/01'
# y = datetime.strptime(datime,"%Y-%m/%d")
# import datetime
#
# aday = timedelta(days=1)
# ys = y + aday
# ya = ys.strftime("%Y-%m/%d")
#
# while True:
#     print(ya)
#     datime = ya
#     print(datime)

from datetime import datetime
import time

# 现在的时间
datime = '2008-01/01'
now = datetime.strptime(datime,"%Y-%m/%d")
# 递增的时间
import datetime
delta = datetime.timedelta(days=1)
dy = now + delta
ya = dy.strftime("%Y-%m/%d")

# 六天后的时间
# endnow = now + datetime.timedelta(days=50)
# # 六天后的时间转换成字符串
# endnow = str(endnow.strftime('%Y-%m-%d'))
#
# offset = now
#
# # 当日期增加到六天后的日期，循环结束
# while str(offset.strftime('%Y-%m-%d')) != endnow:
#     offset += delta
#     print(str(offset.strftime('%Y-%m-%d')))

while True:
    datime = ya
    print(ya)
    dy = now + delta




