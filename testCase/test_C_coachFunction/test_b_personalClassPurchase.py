import unittest
from selenium import webdriver
from pages.coachFunction_page.perclassbuy_page import PerClassBuyPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class PersonalClassBuy(unittest.TestCase):
    """私教购买模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        self.end_data = '2018-12-12'
        self.phone = '16612345678'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().perclassbuy_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['教练功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['私教购买']).click()

    def test_A_buy_perclass(self):  # 失效日期,课程价格,备注,会员手机号
        """添加私教购买测试"""
        PerClassBuyPage(self.driver).A_buy_perclass(self.end_data, self.num[0:3], self.txt, self.phone)

    def test_B_edit_perclass(self):  # 备注
        """编辑私教购买测试"""
        PerClassBuyPage(self.driver).B_edit_perclass(self.txt[::-1])

    def test_C_delete_perclass(self):
        """删除私教购买测试"""
        PerClassBuyPage(self.driver).C_delete_perclass()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
