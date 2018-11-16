import unittest
from selenium import webdriver
from pages.frontDeskFunction_page.cashier_page import CashierPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class Cashier(unittest.TestCase):
    """收银台模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().cashier_page()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['前台功能']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele1['收银台']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['商品管理tab']).click()

    def test_A_add_goods(self):  # 商品条码,商品名称,商品价格
        """添加商品测试"""
        CashierPage(self.driver).A_add_goods(self.num[1:8], self.txt[0:2], self.num[0:2])

    def test_B_edit_goods(self):  # 商品价格
        """编辑商品测试"""
        CashierPage(self.driver).B_edit_goods(self.num[1:3])

    def test_C_goods_entry(self):
        """商品入库测试1"""
        CashierPage(self.driver).C_goods_entry()

    def test_D_add_goods_entry(self):  # 商品条码
        """商品入库测试2"""
        CashierPage(self.driver).D_add_goods_entry(self.num[1:8])

    def test_E_buy_goods(self):  # 商品条码
        """商品购买测试"""
        CashierPage(self.driver).E_buy_goods(self.num[1:8])

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

