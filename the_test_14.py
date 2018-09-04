# coding:utf-8

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()

dr.get("https://www.baidu.com")
dr.find_element_by_name("tj_trnews").click()
window_0 = dr.current_window_handle

try:
    element = WebDriverWait(dr, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="pane-news"]/div/ul/li[1]/strong/a')))
    element.click()
    window_1 = dr.current_window_handle
    windows = dr.window_handles
    print(window_0, window_1, "\n", windows)

    dr.switch_to_window(windows[-1])

    window_1 = dr.current_window_handle
    print(window_0, window_1, "\n", windows)

    time.sleep(5)

finally:
    dr.quit()
