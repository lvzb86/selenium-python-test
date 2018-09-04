# coding:utf-8

from selenium import webdriver

driver = webdriver.Chrome()  # 创建driver对象，启动chrome

driver.get("https://www.google.com")  # 打开网页
driver.get_screenshot_as_file(
    "D:\\Learn\\Selenium_autotest_learn\\screenshot.png")  # 截图并保存为png文件

driver.quit()  # 停止进程
