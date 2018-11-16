import unittest
from selenium import webdriver
from pages.frontDeskFunction_page.vipcard_page import VipCard
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class VipCardManage(unittest.TestCase):
    """会员卡管理测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        self.phone = '18162765452'
        self.start_date = '2018-11-11'
        self.end_date = '2018-12-12'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().vipcardmanage_page()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele1['前台功能']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele1['会员卡管理']).click()
        time.sleep(0.5)

    def test_A_edit_limitcard(self):  # 备注
        """时效卡编辑测试"""
        VipCard(self.driver).A_edit_limitcard(self.txt)

    def test_B_renew_limitcard(self):  # 续卡天数
        """时效卡续卡测试"""
        VipCard(self.driver).B_renew_limitcard(self.num[0:1])

    def test_C_passon_limitcard(self):  # 实付金额,受理人手机号
        """时效卡转卡测试"""
        VipCard(self.driver).C_passon_limitcard(self.num[1:3], self.phone)

    def test_D_stop_limitcard(self):  # 失效开始日期,失效结束日期,实付金额
        """时效卡停卡测试"""
        VipCard(self.driver).D_stop_limitcard(self.start_date, self.end_date, self.num[2:4])

    def test_E_delete_limitcard(self):
        """时效卡删除测试"""
        VipCard(self.driver).E_delete_limitcard()

    def test_F_activate_limitcard(self):
        """时效卡开卡测试"""
        VipCard(self.driver).F_activate_limitcard()

    def test_G_remove_limitcard(self):
        """时效卡彻底删除测试"""
        VipCard(self.driver).G_remove_limitcard()

    def test_H_recover_limitcard(self):
        """时效卡恢复测试"""
        VipCard(self.driver).H_recover_limitcard()

    def test_I_edit_countcard(self):  # 备注
        """次卡编辑测试"""
        VipCard(self.driver).I_edit_countcard(self.txt)

    def test_J_renew_countcard(self):  # 次数
        """次卡续卡测试"""
        VipCard(self.driver).J_renew_countcard(self.num[0:2])

    def test_K_takeout_countcard(self):
        """次卡扣次测试"""
        VipCard(self.driver).K_takeout_countcard()

    def test_L_passon_countcard(self):  # 实付金额,受理人手机号
        """次卡转卡测试"""
        VipCard(self.driver).L_passon_countcard(self.num[1:3], self.phone)

    def test_M_delete_countcard(self):
        """次卡删除测试"""
        VipCard(self.driver).M_delete_countcard()

    def test_N_activate_countcard(self):
        """次卡开卡测试"""
        VipCard(self.driver).N_activate_countcard()

    def test_O_remove_countcard(self):
        """次卡彻底删除测试"""
        VipCard(self.driver).O_remove_countcard()

    def test_P_recover_countcard(self):
        """次卡恢复测试"""
        VipCard(self.driver).P_recover_countcard()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
