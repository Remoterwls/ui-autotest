import unittest
from selenium import webdriver
from pages.advancedSetting_page.protocol_page import ProtocolPage
from pages.registerLogin_page.login_page import LoginPage
from public.data_generate import DataGenerate
from public.ele_manage import EleManage
import time


class TestProtocol(unittest.TestCase):
    """协议模板模块测试"""

    @classmethod
    def setUpClass(self):
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().passage_manage()
        """准备数据"""
        self.phone = '16612345678'
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['高级设置']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['协议模板']).click()

    def test_A_edit_protocol(self):
        """编辑协议测试"""
        ProtocolPage(self.driver).A_edit_protocol()

    def test_B_restart_protocol(self):
        """重置协议测试"""
        ProtocolPage(self.driver).B_restart_protocol()

    def test_C_print_protocol(self):  # 手机号
        """打印协议测试"""
        ProtocolPage(self.driver).C_print_protocol(self.phone)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

