# coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)

# driver.find_element(By.ID, "kw").send_keys("selenium&python")
# driver.find_element(By.ID, "su").click()
# driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]').click()
# driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/span[2]').click()
# 折腾半天才发现定位出来的不是下拉框……
driver.find_element(By.LINK_TEXT, '设置').click()
driver.find_element(By.LINK_TEXT, '搜索设置').click()
time.sleep(2)

sel = driver.find_element(By.XPATH, '//*[@id="nr"]')  # 定位下拉框
Select(sel).select_by_value('50')  # 通过value的值进行选定条目
driver.find_element(By.CLASS_NAME, 'prefpanelgo').click()
time.sleep(2)
driver.switch_to.alert.accept()  # 此处同意警告框提示内容
time.sleep(2)

driver.quit()
