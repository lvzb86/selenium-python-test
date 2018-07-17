# coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()

dr.get("https://www.baidu.com")

dr.find_element_by_xpath('//*[@id="u1"]/a[7]').click()

element = WebDriverWait(dr, 5).until(EC.element_to_be_clickable((
    By.ID, "TANGRAM__PSP_10__footerULoginBtn")))
element.click()

dr.find_element_by_id("TANGRAM__PSP_10__userName").clear()
dr.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("lvae86")
dr.find_element_by_id("TANGRAM__PSP_10__password").clear()
dr.find_element_by_id("TANGRAM__PSP_10__password").send_keys("xiaobin")

try:
    dr.find_element_by_id("TANGRAM__PSP_10__submit").click()
    # 出现验证码，很尴尬啊，难道要单独写个验证码识别模块么
finally:
    time.sleep(5)
    dr.quit()
