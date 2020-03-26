# coding=utf-8
from selenium import webdriver
import time

wd = webdriver.Chrome()  # 打开 Chrome 浏览器
#打开百度浏览器
wd.get('https://www.baidu.com')
# 浏览器最大化
wd.maximize_window()
# 定位输入框并输入关键字
wd.find_element_by_id('kw').send_keys('selenium')
# 点击[百度一下]搜索
wd.find_element_by_id('su').click()
time.sleep(5)
wd.close()  #关闭浏览器
time.sleep(3)
wd.quit()  # 退出浏览器