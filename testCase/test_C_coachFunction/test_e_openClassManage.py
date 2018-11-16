import unittest
from selenium import webdriver
from pages.coachFunction_page.openclass_page import OpenClassPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class OpenClass(unittest.TestCase):
    """公开课模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        self.mix_num = '2'
        self.max_num = '5'
        self.address = '3栋605'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().openclass_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['教练功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['公开课管理']).click()

    def test_A_add_openclass(self):  # 名字,上课地点,最少人数,最大人数
        """添加公开课"""
        OpenClassPage(self.driver).A_add_openclass(self.txt[0:2], self.address, self.mix_num, self.max_num)

    def test_B_edit_openclass(self):  # 名字
        """编辑公开课"""
        OpenClassPage(self.driver).B_edit_openclass(self.txt[1:3])

    def test_C_delete_openclass(self):
        """删除公开课"""
        OpenClassPage(self.driver).C_delete_openclass()

    def test_D_print_openclass(self):
        """打印课表"""
        OpenClassPage(self.driver).D_print_openclass()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
