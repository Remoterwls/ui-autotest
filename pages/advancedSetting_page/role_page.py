import time
from public.ele_manage import EleManage


class RolePage(object):

    def __init__(self, driver):
        self.ele = EleManage().role_manage()
        self.driver = driver

    def A_add_role(self, name, description):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['添加角色按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['角色名称输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['权限模板选择按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['权限模板选择确定按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['角色描述输入框']).send_keys(description)
        self.driver.find_element_by_xpath(self.ele['添加角色确定按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_role(self, name, description):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['编辑角色按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['编辑角色名称输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['编辑角色名称输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['编辑角色描述输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['编辑角色描述输入框']).send_keys(description)
        self.driver.find_element_by_xpath(self.ele['编辑角色确定按钮']).click()
        time.sleep(1)
        return self.driver

    def C_jurisdiction_role(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['权限分配按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['权限分配确定按钮']).click()
        time.sleep(1)
        return self.driver

    def D_delete_role(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['角色删除按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['删除确定按钮']).click()
        time.sleep(1)
        return self.driver
