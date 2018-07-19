# coding=utf-8

import time

from selenium import webdriver

driver = webdriver.Chrome() # 启动chrome
driver.get("https://wwww.google.com") # 打开网址

time.sleep(3) # 暂停5秒

driver.quit()
