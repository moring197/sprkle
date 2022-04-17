# -*- coding:utf-8 -*-
"""
@Time 2021/3/5
@auth 码尚学院_百里老师
@Email 198977131@qq.com
@Content test_login.py
"""
import pytest
from ddt import ddt, data, unpack
from selenium import webdriver

from base.base_util import BaseUtil
from common.excel_util import ExcelUtil
from pageobject.login_page import LoginPage
#@ddt
class TestLogin(BaseUtil):

    # @data(*ExcelUtil().read_excel())
    # @unpack
    @pytest.mark.parametrize("index,username,password",ExcelUtil().read_excel())
    def test_01_login(self,index,username,password):
        """ 登录 """
        lp = LoginPage(self.driver)
        lp.login_ecshop(username,password)
        if index==1:
            # 断言
            #self.assertEqual(lp.get_except_result(),'退出')
            assert lp.get_except_result() == '退出'

