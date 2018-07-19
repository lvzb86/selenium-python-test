# coding=utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)

# 键盘事件
driver.find_element(By.ID, 'kw').send_keys("selenium&python?")
time.sleep(3)
driver.find_element(By.ID, 'kw').send_keys(
    Keys.BACK_SPACE)  # 利用backspace键删除字符串最后一位
time.sleep(3)
driver.find_element(By.ID, 'kw').send_keys(Keys.SPACE)  # 在字符串后空格键添加空格
driver.find_element(By.ID, 'kw').send_keys("学习")  # 继续在字符串后面添加字符串
driver.find_element(By.ID, 'kw').send_keys(Keys.ENTER)  # 输入回车enter键进行搜索
time.sleep(3)

driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'a')  # 全选搜索框中的内容
driver.find_element(By.ID, 'kw').send_keys(
    Keys.CONTROL, 'x')  # 剪切搜索框中的内容，也可以使用c进行复制
time.sleep(3)

# 打开另外一个搜索网站，输入刚刚剪切的内容
driver.get("https://www.google.com")
driver.find_element(By.ID, 'lst-ib').send_keys(Keys.CONTROL,
                                               'v')  # 粘贴刚刚复制、剪切的内容
driver.find_element(By.ID, 'lst-ib').submit()  # 提交搜索

time.sleep(3)
"""
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）

send_keys(Keys.SPACE) 空格键(Space)

send_keys(Keys.TAB) 制表键(Tab)

send_keys(Keys.ESCAPE) 回退键（Esc）

send_keys(Keys.ENTER) 回车键（Enter）

send_keys(Keys.CONTROL, ‘a’) 全选（Ctrl+A）

send_keys(Keys.CONTROL, ‘c’) 复制（Ctrl+C）

send_keys(Keys.CONTROL, ‘x’) 剪切（Ctrl+X）

send_keys(Keys.CONTROL, ‘v’) 粘贴（Ctrl+V）

send_keys(Keys.F1) 键盘 F1
...
send_keys(Keys.F12) 键盘 F12
"""
driver.quit()
