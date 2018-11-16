import unittest
from selenium import webdriver
from pages.registerLogin_page.register_page import RegisterPage
from public.read_cfg import ReadCfg


class TestRegister(unittest.TestCase):
    """注册测试"""

    def setUp(self):
        print('注册测试开始')
        self.driver = webdriver.Chrome()
        self.url = ReadCfg().get_login_url_info()['登录url']

    def test_register(self):
        """注册流程测试"""
        self.driver = RegisterPage(self.driver).register()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="app"]/div/div[6]/h2').text, '注册完成', '注册测试失败')

    def tearDown(self):
        print('注册测试结束')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



