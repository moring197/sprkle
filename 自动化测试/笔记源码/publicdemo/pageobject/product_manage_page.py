# -*- coding:utf-8 -*-
"""
@Time 2021/3/5
@auth 码尚学院_百里老师
@Email 198977131@qq.com
@Content product_manage_page.py
"""
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pageobject.login_page import LoginPage


class ProductManagePage(BasePage):

    #页面元素
    product_list_loc = (By.LINK_TEXT,"商品列表")
    cat_id_loc =  (By.NAME,"cat_id")
    sousuo_loc = (By.XPATH,"//input[@value=' 搜索 ']")
    #页面动作
    def select_product(self,value):
        #登录
        lp = LoginPage(self.driver)
        lp.login_ecshop()
        #查询
        self.goto_frame("menu-frame")
        self.click(ProductManagePage.product_list_loc)
        self.quit_frame()
        self.goto_frame("main-frame")
        self.choice_select(ProductManagePage.cat_id_loc,value)
        self.click(ProductManagePage.sousuo_loc)