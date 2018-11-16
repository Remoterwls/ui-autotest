import unittest
from selenium import webdriver
from pages.menbershipFunction_page.membership_page import MemberShipPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class MemberShip(unittest.TestCase):
    """客户管理模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.phone = DataGenerate().create_phone()
        self.birth = '2018-10-01'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().membership_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['会籍功能']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele1['客户管理']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜在客户tab']).click()
        time.sleep(0.5)

    def test_A_add_potential_customers(self):  # 姓名,手机号,备注
        """添加潜客测试"""
        MemberShipPage(self.driver).A_add_potential_customers(self.txt[0:2], self.phone, self.txt)

    def test_B_edit_potential_customers(self):  # 生日
        """编辑潜客测试"""
        MemberShipPage(self.driver).B_edit_potential_customers(self.birth)

    def test_C_distribute_member(self):
        """潜客分配会籍测试"""
        MemberShipPage(self.driver).C_distribute_member()

    def test_D_distribute_coach(self):
        """潜客分配教练测试"""
        MemberShipPage(self.driver).D_distribute_coach()

    def test_E_delete_potential_customers(self):
        """潜客删除测试"""
        MemberShipPage(self.driver).E_delete_potential_customers()

    def test_F_recovery_potential_customers(self):
        """潜客恢复测试"""
        MemberShipPage(self.driver).F_recovery_potential_customers()

    def test_G_edit_vip(self):  # 生日
        """编辑会员测试"""
        MemberShipPage(self.driver).G_edit_vip(self.birth)

    def test_H_distribute_vipmember(self):
        """会员分配会籍测试"""
        MemberShipPage(self.driver).H_distribute_vipmember()

    def test_I_distribute_vipcoach(self):
        """会员分配教练测试"""
        MemberShipPage(self.driver).I_distribute_vipcoach()

    def test_J_delete_vip(self):
        """删除会员测试"""
        MemberShipPage(self.driver).J_delete_vip()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
