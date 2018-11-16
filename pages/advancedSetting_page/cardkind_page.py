import time
from public.ele_manage import EleManage


class CardKindPage(object):

    def __init__(self, driver):
        self.ele = EleManage().cardKind_manage()
        self.driver = driver

    def A_add_card(self, name, day, price, remark):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['添加卡种按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['卡种名称输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['卡种封面选择按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['卡种封面确定按钮']).click()
        self.driver.find_element_by_xpath(self.ele['时效卡天数输入框']).send_keys(day)
        self.driver.find_element_by_xpath(self.ele['底价输入框']).send_keys(price)
        self.driver.find_element_by_xpath(self.ele['价格输入框']).send_keys(price)
        self.driver.find_element_by_xpath(self.ele['SAAS上架选择按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['SAAS上架确定按钮']).click()
        self.driver.find_element_by_xpath(self.ele['备注输入框']).send_keys(remark)
        self.driver.find_element_by_xpath(self.ele['添加卡种确定按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_card(self, name):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['编辑卡种按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['卡种名称输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['卡种名称输入框']).send_keys(name)
        self.driver.find_element_by_xpath(self.ele['编辑卡种更新按钮']).click()
        time.sleep(1)
        return self.driver

    def C_delete_card(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['卡种删除按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['卡种删除确定按钮']).click()
        time.sleep(1)
        return self.driver
