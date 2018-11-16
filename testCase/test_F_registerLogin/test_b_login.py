import unittest
from selenium import webdriver
from pages.registerLogin_page.login_page import LoginPage


class TestLogin(unittest.TestCase):
    """登录测试"""

    def setUp(self):
        print('登录测试开始')
        self.driver = webdriver.Chrome()

    def test_login(self):
        """正常登录测试"""
        self.driver = LoginPage(self.driver).login()
        self.assertEqual(self.driver.find_element_by_xpath('//*[@id="app"]/div/ul/div[1]').text, '测试俱乐部02', '登录测试失败')

    def tearDown(self):
        print('登录测试结束')
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
