import unittest
from selenium import webdriver
from pages.coachFunction_page.groupclass_page import GroupClassPage
from public.data_generate import DataGenerate
from pages.registerLogin_page.login_page import LoginPage
from public.ele_manage import EleManage
import time


class GroupClass(unittest.TestCase):
    """团课模块测试"""

    @classmethod
    def setUpClass(self):
        """准备数据"""
        self.txt = DataGenerate().create_txt()
        self.num = DataGenerate().create_phone()
        self.phone = '16612345678'
        self.start_date = '2018-11-11'
        self.end_date = '2018-12-12'
        self.start_time = '18:00'
        self.end_time = '23:30'
        self.end_new_time = '23:00'
        self.min_num = '2'
        self.max_num = '5'
        self.address = '3栋605'
        """准备元素"""
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().groupclass_manage()
        """启动浏览器"""
        self.driver = webdriver.Chrome()
        self.driver = LoginPage(self.driver).login()
        self.driver.find_element_by_xpath(self.ele1['教练功能']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele1['团课管理']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['团课课程tab']).click()

    def test_A_add_groupclass(self):  # 课程名,价格,上课地点,最少人数,最多人数
        """添加团课测试"""
        GroupClassPage(self.driver).A_add_groupclass(self.txt[0:2], self.num[0:2], self.address, self.min_num, self.max_num)

    def test_B_edit_groupclass(self):  # 课程名
        """编辑团课测试"""
        GroupClassPage(self.driver).B_edit_groupclass(self.txt[1:3])

    # @unittest.skip('xxx')
    def test_C_queuing_groupclass(self):  # 开始日期,结束日期,开始时间,结束时间
        """团课排期测试"""
        GroupClassPage(self.driver).C_queuing_groupclass(self.start_date, self.end_date, self.start_time, self.end_time)

    def test_D_delete_groupclass(self):
        """删除团课测试"""
        GroupClassPage(self.driver).D_delete_groupclass()

    def test_E_add_queuing(self):  # 开始日期,结束日期,开始时间,结束时间
        """添加排期测试"""
        GroupClassPage(self.driver).E_add_queuing(self.start_date, self.end_date, self.start_time, self.end_time)

    def test_F_edit_queuing(self):  # 结束时间
        """编辑排期测试"""
        GroupClassPage(self.driver).F_edit_queuing(self.end_new_time)

    def test_G_order_class(self):  # 价格,会员手机号
        """预约团课测试"""
        GroupClassPage(self.driver).G_order_class(self.num[1:4], self.phone)

    @unittest.skip('未知错误，相对位置也无法定位元素')
    def test_H_cancel_class(self):
        """取消预约测试"""
        GroupClassPage(self.driver).H_cancel_class()

    def test_I_delete_queuing(self):
        """删除排期测试"""
        GroupClassPage(self.driver).I_delete_queuing()

    def test_J_print_groupclass(self):
        """打印课表测试"""
        GroupClassPage(self.driver).J_print_groupclass()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
