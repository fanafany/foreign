# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-08 15:12 '


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from mouse import move,click
from time import sleep
import re
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome(executable_path ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.maximize_window()
dates = []
browser.get('https://pangu.songshuai.com/#/login')
sleep(1)
user = browser.find_element_by_xpath("//input[@type='text']").send_keys('13764110015')
sleep(1)
pwd = browser.find_element_by_xpath("//input[@type='Password']").send_keys('wlh57362376')
sleep(1)
sub = browser.find_element_by_xpath("//button[@type='button']/span[1]").click()
sleep(5)
# ghc = browser.find_element_by_xpath("//span[@title='公海池']").click()
move(64,444)
click()
sleep(3)


move(464,379)
click()
sleep(3)

login_moble = re.search(r'<!---->1(.*?)</div>',browser.page_source).group(0)
login_0 = login_moble.replace('<!---->','').replace('</div>','')
print(login_0)
# dates.append(moble_1)
move(459,431)
click()
sleep(2)
login_moble_1 = re.search(r'<!---->1(.*?)</div>',browser.page_source).group(0)
login_1 = login_moble_1.replace('<!---->','').replace('</div>','')
print(login_1)
print(browser.page_source)










print('执行成功')

sleep(3)


'''
http://bid.cdt-ec.com/dtdzzb/loginController.do?login&amp;bulletinId=8af894dc6f84b354016fc324d8c6602c&quot;,
&quot;http://bid.cdt-ec.com/project/2020-01/a4216b5e4a4f4129ba12be10ebb999e7/createBulletinContentFile/7345564643ff46b9a775a033b2c7ad72.swf&quot;,
&quot;http://bid.cdt-ec.com/dtdzzb/cgUploadController.do?downLoadFileOut&amp;extend=pdf&amp;objId=8af894dd6f84af8f016fc348e9be04fb&quot;)"
'''

