import time
from public.ele_manage import EleManage


class ProtocolPage(object):

    def __init__(self, driver):
        self.ele = EleManage().protocol_manage()
        self.driver = driver

    def A_edit_protocol(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['编辑协议按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['编辑协议保存按钮']).click()
        time.sleep(1)
        return self.driver

    def B_restart_protocol(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['协议重置按钮']).click()
        time.sleep(1)
        return self.driver

    def C_print_protocol(self, phone):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['手机号输入框']).send_keys(phone)
        self.driver.find_element_by_xpath(self.ele['搜索图标']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['打印协议按钮']).click()
        time.sleep(1)
        return self.driver

