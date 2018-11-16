import unittest
from selenium import webdriver
from pages.coachFunction_page.perorder_page import PerOrderPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class PersonalClassOrder(unittest.TestCase):
    """私教预约模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.phone = '16612345678'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().perclassorder_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['教练功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['私教预约']).click()

    def test_A_order_perclass(self):  # 会员手机号
        """添加私教课预约测试"""
        PerOrderPage(self.driver).A_order_perclass(self.phone)

    @unittest.skip('无法消课，需配合手机端')
    def test_B_finish_perclass(self):
        """私教消课测试"""
        PerOrderPage(self.driver).B_finish_perclass()

    def test_C_cancel_perclass(self):
        """取消私教课预约测试"""
        PerOrderPage(self.driver).C_cancel_perclass()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
