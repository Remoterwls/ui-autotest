import unittest
from selenium import webdriver
from pages.advancedSetting_page.role_page import RolePage
from pages.registerLogin_page.login_page import LoginPage
from public.data_generate import DataGenerate
from public.ele_manage import EleManage
import time


class TestRoleManage(unittest.TestCase):
    """角色管理模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().role_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['高级设置']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['角色管理']).click()

    def test_A_add_role(self):  # 角色名称,角色描述
        """添加角色测试"""
        RolePage(self.driver).A_add_role(self.txt[0:2], self.txt)

    def test_B_edit_role(self):  # 角色名称,角色描述
        """编辑角色测试"""
        RolePage(self.driver).B_edit_role(self.txt[1:3], self.txt[::-1])

    def test_C_jurisdiction_role(self):
        """权限分配测试"""
        RolePage(self.driver).C_jurisdiction_role()

    def test_D_delete_role(self):
        """删除角色测试"""
        RolePage(self.driver).D_delete_role()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
