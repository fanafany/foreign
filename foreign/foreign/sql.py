# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-08 15:12 '


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from mouse import move,click
from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome(executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.maximize_window()
browser.get('http://www.cdt-ec.com/home/')
sleep(1)
title = browser.find_element_by_xpath('//div[@class="content"]/div[2]/ul[2]/button[3]').click()
sleep(1)
user = browser.find_element_by_xpath("//div[@class='highly-login-box']/div[2]/input").send_keys('北京合信锐风新能源发展有限公司')

pwd = browser.find_element_by_xpath("//div[@class='highly-login-box']/div[3]/input").send_keys('hxrf6688')
sleep(1)
sub = browser.find_element_by_xpath("//div[@class='highly-login-box']/div[4]/input").click()
sleep(12)
move(1138,198)
click()
sleep(3)
bids = browser.find_element_by_xpath('//div[@class="navigation"]/ul/a[4]/li').click()
sleep(2)
text = browser.find_element_by_xpath("//li/input[@id='message_title']").send_keys('无功补偿')
inquire = browser.find_element_by_xpath("//div[@class='classs']/ul/li[4]/input").click()
print(browser.page_source)


print('执行成功')

sleep(3)


'''
http://bid.cdt-ec.com/dtdzzb/loginController.do?login&amp;bulletinId=8af894dc6f84b354016fc324d8c6602c&quot;,
&quot;http://bid.cdt-ec.com/project/2020-01/a4216b5e4a4f4129ba12be10ebb999e7/createBulletinContentFile/7345564643ff46b9a775a033b2c7ad72.swf&quot;,
&quot;http://bid.cdt-ec.com/dtdzzb/cgUploadController.do?downLoadFileOut&amp;extend=pdf&amp;objId=8af894dd6f84af8f016fc348e9be04fb&quot;)"
'''

