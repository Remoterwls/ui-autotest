import time
from public.ele_manage import EleManage


class ClubPage(object):

    def __init__(self, driver):
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().club_manage()
        self.driver = driver

    def A_edit_clubMessage(self, name, phone, address):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['修改俱乐部信息按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['场馆名称输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['场馆名称输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['场馆电话输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['场馆电话输入框']).send_keys(phone)
        self.driver.find_element_by_xpath(self.ele['场馆地址输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['场馆地址输入框']).send_keys(address)
        self.driver.find_element_by_xpath(self.ele['保存修改按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_legalPerson(self, name, name2):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['法人信息认证按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['账户名称输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['账户名称输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['开户行-支行输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['开户行-支行输入框']).send_keys(name2)
        self.driver.find_element_by_xpath(self.ele['提交认证按钮']).click()
        time.sleep(1)
        return self.driver
