# coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开一个网页
driver.get("https://www.zhihu.com/")

# 查找一个元素的方法
ele = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/header/div/nav/a[2]')
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

ele.click() # 点击已定位的元素
driver.back() # 退回

time.sleep(5)
ele = driver.find_element(
    By.XPATH, '//*[@id="root"]/div/div[2]/header/div/nav/a[2]')
# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

ele.click()
driver.back()

# 查找多个元素的方法
eles = driver.find_elements_by_class_name("Feed")
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

print(eles)
print(len(eles))

time.sleep(5)
eles = driver.find_elements(By.CLASS_NAME, 'Feed')
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

print(eles)
print(len(eles))

driver.quit()
