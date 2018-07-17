# coding:utf-8

from selenium import webdriver

dr = webdriver.Chrome()

dr.get("https://mail.163.com/")

dr.switch_to_frame("x-URS-iframe")
dr.find_element_by_name("email").clear()
dr.find_element_by_name("email").send_keys("username")
dr.find_element_by_name("password").clear()
dr.find_element_by_name("password").send_keys("password")
dr.find_element_by_id("dologin").click()
dr.switch_to_default_content()

dr.quit()
