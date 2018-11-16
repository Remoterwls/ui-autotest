import unittest
from selenium import webdriver
from pages.coachFunction_page.sidereport_page import SideReportPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class SideReport(unittest.TestCase):
    """体侧报告模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        self.phone = '16612345678'
        self.time = '2018-10-01 19:31:34'
        self.age = '22'
        self.height = '181'
        self.weight = '100'
        self.other = '11'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().sidereport_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['教练功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['体侧报告']).click()

    def test_A_add_sideReport(self):  # 会员手机号,体测时间,年龄,身高,体重,其他
        """添加体侧报告测试"""
        SideReportPage(self.driver).A_add_sideReport(self.phone, self.time, self.age, self.height, self.weight, self.other)

    def test_B_edit_sideReport(self):  # 其他
        """编辑体侧报告测试"""
        SideReportPage(self.driver).B_edit_sideReport(self.num[0:2])

    def test_C_look_sideReport(self):
        """查看体测报告测试"""
        SideReportPage(self.driver).C_look_sideReport()

    def test_D_delete_sideReport(self):
        """删除体侧报告测试"""
        SideReportPage(self.driver).D_delete_sideReport()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
