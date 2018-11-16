import unittest
from selenium import webdriver
from pages.advancedSetting_page.cardkind_page import CardKindPage
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
from public.data_generate import DataGenerate
import time


class TestCardManage(unittest.TestCase):
    """卡种管理模块测试"""

    @classmethod
    def setUpClass(self):
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().cardKind_manage()
        """准备数据"""
        self.num = DataGenerate().create_phone()
        self.txt = DataGenerate().create_txt()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['高级设置']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['卡种管理']).click()

    def test_A_add_card(self):  # 卡种名称,天数,底价=价格,备注
        """添加卡种测试"""
        CardKindPage(self.driver).A_add_card(self.txt[0:2], self.num[0:2], self.num[1:3], self.txt)

    def test_B_edit_card(self):  # 卡种名称
        """编辑卡种测试"""
        CardKindPage(self.driver).B_edit_card(self.txt[1:3])

    def test_C_delete_card(self):
        """删除卡种测试"""
        CardKindPage(self.driver).C_delete_card()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


