# coding:utf-8
# 强制等待——代码休眠
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)

driver.quit()
