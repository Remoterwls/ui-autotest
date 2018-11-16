import unittest
from selenium import webdriver
from pages.storeManageFunction_page.staff_page import StaffManage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class TestStaff(unittest.TestCase):
    """员工管理测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().staff_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['店长功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['员工管理']).click()

    def test_A_add_staff(self):  # 员工姓名
        """添加员工测试"""
        StaffManage(self.driver).A_add_staff(self.txt[0:2])

    def test_B_edit_staff(self):  # 员工姓名
        """编辑员工测试"""
        StaffManage(self.driver).B_edit_staff(self.txt[1:3])

    def test_C_forbidden_staff(self):
        """禁用员工测试"""
        StaffManage(self.driver).C_forbidden_staff()

    def test_D_restart_staff(self):
        """启用员工测试"""
        StaffManage(self.driver).D_restart_staff()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
