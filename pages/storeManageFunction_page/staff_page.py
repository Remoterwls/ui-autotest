from public.ele_manage import EleManage
import time
import os


class StaffManage(object):

    def __init__(self, driver):
        self.ele = EleManage().staff_manage()
        self.driver = driver

    def A_add_staff(self, name):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['添加员工按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['姓名输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['角色选择按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['角色选择确定按钮']).click()
        self.driver.find_element_by_xpath(self.ele['上传员工头像按钮']).click()
        self.driver.find_element_by_xpath(self.ele['上传员工头像弹出按钮']).click()
        os.system(r'D:\UI\testFile\LOGO001.exe')
        self.driver.find_element_by_xpath(self.ele['上传员工头像保存按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['添加员工提交按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_staff(self, name):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['员工编辑按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['员工编辑姓名输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['员工编辑姓名输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['员工编辑提交按钮']).click()
        time.sleep(1)
        return self.driver

    def C_forbidden_staff(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['禁用员工按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['禁用员工确定按钮']).click()
        time.sleep(1)
        return self.driver

    def D_restart_staff(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['切换到禁用table']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele['启用员工按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['启用员工确定按钮']).click()
        time.sleep(1)
        return self.driver


