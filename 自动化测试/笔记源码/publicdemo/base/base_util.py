# -*- coding:utf-8 -*-
"""
@Time 2021/3/5
@auth 码尚学院_百里老师
@Email 198977131@qq.com
@Content base_util.py
"""
import time

from selenium import webdriver

class BaseUtil:

    def setup(self) -> None:
        global driver
        # 打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 加载网页
        self.driver.get("http://localhost/ecshop/admin/privilege.php?act=logout")

    def teardown(self) -> None:
        time.sleep(3)
        self.driver.quit()