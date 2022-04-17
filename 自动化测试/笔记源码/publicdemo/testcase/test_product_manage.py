# -*- coding:utf-8 -*-
"""
@Time 2021/3/4
@auth 码尚学院_百里老师
@Email 198977131@qq.com
@Content test_product_manage.py
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_util import BaseUtil
from pageobject.login_page import LoginPage
from pageobject.product_manage_page import ProductManagePage

class TestProductManage(BaseUtil):

    def aaatest_03_select_product(self):
        """ 查询商品 """
        pm = ProductManagePage(self.driver)
        pm.select_product("4")

    # def test_02_add_product(self):
    #     """
    #     增加新商品
    #     :return:
    #     """
    #     # 登录
    #     global driver
    #     # 打开浏览器
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(10)
    #     # 加载网页
    #     driver.get("http://localhost/ecshop/admin/privilege.php?act=logout")
    #     # 输入用户名和密码
    #     driver.find_element(By.NAME, "username").send_keys("admin")
    #     driver.find_element(By.NAME, "password").send_keys("admin123")
    #     # 点击登录
    #     driver.find_element(By.XPATH, "//input[@value='进入管理中心']").click()
    #     # 查询商品
    #     # 进入菜单框架
    #     driver.switch_to.frame("menu-frame")
    #     # 点击商品列表
    #     driver.find_element(By.LINK_TEXT, "添加新商品").click()
    #     # 出框架
    #     driver.switch_to.default_content()
    #     # 进入到main的框架
    #     driver.switch_to.frame("main-frame")
    #     #---------增加---------------------
    #     #输入商品名称
    #     driver.find_element(By.NAME,"goods_name").send_keys("码尚学院VIP")
    #     #选择商品分类
    #     sel = Select(driver.find_element(By.NAME,"cat_id"))
    #     sel.select_by_value("12")
    #     #输入价格
    #     shop_price = driver.find_element(By.NAME,"shop_price")
    #     shop_price.clear()
    #     shop_price.send_keys("6880")
    #     #上传图片
    #     driver.find_element(By.NAME,"goods_img").send_keys(r"E:/shu.png")
    #     #点击确定
    #     driver.find_element(By.XPATH,"//input[@value=' 确定 ']").click()
    #

    # def test_04_delete_product(self):
    #     # 登录
    #     global driver
    #     # 打开浏览器
    #     driver = webdriver.Chrome()
    #     driver.implicitly_wait(10)
    #     # 加载网页
    #     driver.get("http://localhost/ecshop/admin/privilege.php?act=logout")
    #     # 输入用户名和密码
    #     driver.find_element(By.NAME, "username").send_keys("admin")
    #     driver.find_element(By.NAME, "password").send_keys("admin123")
    #     # 点击登录
    #     driver.find_element(By.XPATH, "//input[@value='进入管理中心']").click()
    #     # 查询商品
    #     # 进入菜单框架
    #     driver.switch_to.frame("menu-frame")
    #     # 点击商品列表
    #     driver.find_element(By.LINK_TEXT, "商品列表").click()
    #     # 出框架
    #     driver.switch_to.default_content()
    #     # 进入到main的框架
    #     driver.switch_to.frame("main-frame")
    #     #-------------删除-------------------
    #     del_button_list = driver.find_elements(By.XPATH,"//img[@src='images/icon_trash.gif']")
    #     if len(del_button_list)>0:
    #         del_button_list[0].click()
    #     else:
    #         print("没有可以删除的数据")
    #     #处理弹出窗口：alert(只有确定),confirm(有确定有取消),prompt（有确定有取消还可以输入值）
    #     time.sleep(3)
    #     ale = driver.switch_to.alert
    #     ale.accept()
    #     #access点击确定，dismiss点击取消，text获得文本,send_keys输入值

if __name__ == '__main__':
    unittest.main()

