import unittest
from selenium import webdriver
from pages.advancedSetting_page.passage_page import PassageManage
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
from public.data_generate import DataGenerate
import time


class TestPassage(unittest.TestCase):
    """文章推送模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().passage_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['高级设置']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['文章推送']).click()

    def test_A_addpassage(self):  # 文章标题,文章摘要,文章内容
        """添加文章测试"""
        PassageManage(self.driver).A_add_passage(self.txt[0:2], self.txt[1:8], self.txt)

    def test_B_editpassage(self):  # 文章标题
        """编辑文章测试"""
        PassageManage(self.driver).B_edit_passage(self.txt[1:3])

    def test_C_searchpassage(self):  # 文章标题
        """搜索文章测试"""
        PassageManage(self.driver).C_search_passage(self.txt[1:3])

    def test_D_delpassage(self):
        """删除文章测试"""
        PassageManage(self.driver).D_del_passage()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()