# coding:utf-8

import time
import unittest

from selenium import webdriver

dr = webdriver.Chrome()

dr.maximize_window()

dr.get("https://www.baidu.com")
print(dr.title)

def test_title(self):
   self.assertEqual("百度一下，你就知道", dr.title)


time.sleep(5)

dr.quit()

if __name__ == '__main__':
    unittest.main()
