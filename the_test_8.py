# coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
time.sleep(3)

# 定位元素
ele_1 = driver.find_element(By.XPATH, '//*[@id="u1"]/a[9]')
ele_2 = driver.find_element(By.XPATH, '//*[@id="u1"]/a[8]')

# 将鼠标悬停在元素1上3秒后再次悬停到元素2上
ActionChains(driver).move_to_element(ele_1).perform()
time.sleep(3)
ActionChains(driver).move_to_element(ele_2).perform()
time.sleep(3)

driver.quit()


"""
click(on_element=None) ——单击鼠标左键

click_and_hold(on_element=None) ——点击鼠标左键，不松开

context_click(on_element=None) ——点击鼠标右键

double_click(on_element=None) ——双击鼠标左键

drag_and_drop(source, target) ——拖拽到某个元素然后松开

drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开

key_down(value, element=None) ——按下某个键盘上的键

key_up(value, element=None) ——松开某个键

move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标

move_to_element(to_element) ——鼠标移动到某个元素

move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置

perform() ——执行链中的所有动作

release(on_element=None) ——在某个元素位置松开鼠标左键

send_keys(*keys_to_send) ——发送某个键到当前焦点的元素

send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素
"""