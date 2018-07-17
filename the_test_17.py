# coding:utf-8

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    def login(self, username, password):
        self.dr.get("https://passport.cnblogs.com/user/signin")
        self.dr.find_element_by_id("input1").send_keys(username)
        self.dr.find_element_by_id("input2").send_keys(password)
        self.dr.find_element_by_id("signin").click()

    def verify(self, username, password, id):
        self.login(username, password)

        element = WebDriverWait(self.dr, 5).until(
            EC.presence_of_element_located((By.ID, id)))

        return element

    def test_login_success(self):
        '''用户名正确、密码正确'''
        element = self.verify("username", "password", "lnk_current_user")

        # self.login("username", "password")

        # element = WebDriverWait(self.dr, 5).until(
        #     EC.presence_of_element_located((By.ID,
        #  "lnk_current_user")))
        self.assertTrue('username' in element.text)

        self.dr.get_screenshot_as_file("D:\\test_img\\login_success.jpg")

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        element = self.verify("username", "errorpassword", "tip_btn")

        # self.login("username", "errorpassword")

        # element = WebDriverWait(self.dr, 5).until(
        #     EC.presence_of_element_located((By.ID, "tip_btn")))
        self.assertIn("用户名或密码错误", element.text)

        self.dr.get_screenshot_as_file("D:\\test_img\\login_success.jpg")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        element = self.verify("username", "", "tip_input2")
        # self.login("username", "")

        # element = WebDriverWait(self.dr, 5).until(
        #     EC.presence_of_element_located((By.ID, "tip_input2")))
        self.assertEqual(element.text, "请输入密码")

        self.dr.get_screenshot_as_file("D:\\test_img\\login_pwd_null.jpg")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        element = self.verify("errorusername", "password", "tip_btn")
        # self.login("errorusername", "password")

        # element = WebDriverWait(self.dr, 5).until(
        #     EC.presence_of_element_located((By.ID, "tip_btn")))
        self.assertIn("该用户不存在", element.text)

        self.dr.get_screenshot_as_file("D:\\test_img\\login_user_error.jpg")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        element = self.verify("", "password", "tip_input1")
        # self.login("", "password")

        # element = WebDriverWait(self.dr, 5).until(
        #     EC.presence_of_element_located((By.ID, "tip_input1")))
        self.assertEqual(element.text, "请输入登录用户名")

        self.dr.get_screenshot_as_file("D:\\test_img\\login_user_null.jpg")

    def tearDown(self):

        print("完成测试")

        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
