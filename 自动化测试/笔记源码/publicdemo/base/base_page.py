# -*- coding:utf-8 -*-
"""
@Time 2021/3/5
@auth 码尚学院_百里老师
@Email 198977131@qq.com
@Content base_page.py
"""
from selenium.webdriver.support.select import Select

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    #定位元素的关键字
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

    #设置值的关键字
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    #单击的关键字
    def click(self,loc):
        self.locator_element(loc).click()

    #进入框架的关键字
    def goto_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    #出框架的关键字
    def quit_frame(self):
        self.driver.switch_to.default_content()

    #封装选中下拉框关键字
    def choice_select(self,loc,value):
        sel = Select(self.locator_element(loc))
        sel.select_by_value(value)

    #获取文本的值
    def get_value(self,loc):
        return self.locator_element(loc).text
