import unittest
from selenium import webdriver
from pages.coachFunction_page.permanage_page import PerManagePage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class PersonalClass(unittest.TestCase):
    """私教课程模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        self.end_data = '2018-12-12'
        self.phone = '16612345678'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().perclass_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['教练功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['私教课程']).click()

    def test_A_add_perclass(self):  # 课程名,课程介绍
        """添加私教课测试"""
        PerManagePage(self.driver).A_add_perclass(self.txt[0:2], self.txt)

    def test_B_edit_perclass(self):  # 课程名
        """编辑私教课测试"""
        PerManagePage(self.driver).B_edit_perclass()

    def test_C_add_percoach(self):  # 课程价格
        """添加私教课教练测试"""
        PerManagePage(self.driver).C_add_percoach(self.num[0:3])

    def test_D_edit_percoach(self):  # 课程价格
        """编辑私教课教练测试"""
        PerManagePage(self.driver).D_edit_percoach(self.num[1:3])

    def test_E_buy_perclass(self):  # 失效日期,课程价格,课程描述,会员手机号
        """私教课购买测试"""
        PerManagePage(self.driver).E_buy_perclass(self.end_data, self.num[0:4], self.txt, self.phone)

    @unittest.skip('不能删除带课教练，不然私教购买无法进行')
    def test_F_delete_percoach(self):
        """删除私教课教练测试"""
        PerManagePage(self.driver).F_delete_percoach()

    @unittest.skip('不能删除课程，不然私教购买无法进行')
    def test_G_delete_perclass(self):
        """删除私教课测试"""
        PerManagePage(self.driver).G_delete_perclass()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

