# coding:utf-8

import time

from selenium import webdriver

dr = webdriver.Chrome()
dr.maximize_window()

dr.get("https://www.baidu.com")
print(dr.title)

try:
    assert (dr.title == "百度一下，你就知道")
except:
    print('标题错误，请查看错误信息')


time.sleep(5)
dr.quit()
