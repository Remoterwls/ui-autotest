import unittest
from selenium import webdriver
from pages.advancedSetting_page.club_page import ClubPage
from pages.registerLogin_page.login_page import LoginPage
from public.data_generate import DataGenerate
from public.ele_manage import EleManage
import time


class TestClubManage(unittest.TestCase):
    """俱乐部信息模块测试"""

    @classmethod
    def setUpClass(self):
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().club_manage()
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.phone = DataGenerate().create_phone()
        self.address = '武汉市光谷软件园'
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['高级设置']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['俱乐部信息']).click()

    def test_A_edit_clubMessage(self):  # 场馆名称,场馆电话,场馆地址
        """编辑俱乐部信息测试"""
        ClubPage(self.driver).A_edit_clubMessage(self.txt[0:5], self.phone, self.address)

    def test_B_edit_legalPerson(self):  # 账户名称, 开户行名称
        """编辑法人信息测试"""
        ClubPage(self.driver).B_edit_legalPerson(self.txt[1:5], self.txt[0:4])

    @classmethod
    def tearDownClass(self):
        print('俱乐部信息模块测试结束')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
