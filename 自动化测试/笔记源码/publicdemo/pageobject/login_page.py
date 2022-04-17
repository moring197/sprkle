# -*- coding:utf-8 -*-
"""
@Time 2021/3/5
@auth 码尚学院_百里老师
@Email 198977131@qq.com
@Content login_page.py
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):

    #页面的元素
    username_loc = (By.NAME,"username")
    password_loc = (By.NAME,"password")
    submit_loc = (By.XPATH,"//input[@value='进入管理中心']")
    tuichu_loc = (By.LINK_TEXT,'退出')

    #页面的动作
    def login_ecshop(self,username="admin",password="admin123"):
        self.send_keys(LoginPage.username_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.submit_loc)

    #断言
    def get_except_result(self):
        self.goto_frame("header-frame")
        return self.get_value(LoginPage.tuichu_loc)