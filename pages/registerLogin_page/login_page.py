from selenium import webdriver
from public.read_cfg import ReadCfg
import time
from public.ele_manage import EleManage


class LoginPage(object):

    def __init__(self, driver):
        """准备数据"""
        self.account = ReadCfg().get_login_account_info()['登录账号']
        self.pwd = ReadCfg().get_login_account_info()['登录密码']
        self.url = ReadCfg().get_login_url_info()['登录url']
        """准备元素字典"""
        self.ele = EleManage().login_manage()
        self.driver = driver
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.find_element_by_name(self.ele['账号输入框']).send_keys(self.account)
        self.driver.find_element_by_name(self.ele['密码输入框']).send_keys(self.pwd)
        self.driver.find_element_by_xpath(self.ele['登录按钮']).click()
        time.sleep(1)
        return self.driver


if __name__ == "__main__":
    d = webdriver.Chrome()
    LoginPage(d).login()
