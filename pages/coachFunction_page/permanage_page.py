import time
from public.ele_manage import EleManage


class PerManagePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().perclass_manage()

    def A_add_perclass(self, name, description):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课按钮']).click()
        time.sleep(0.5)
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['添加私教课确定按钮'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        EleManage().located_by_xpath(self.driver, self.ele['课程名称输入框']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['课程类型选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程类型选择确定按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['课程时长选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程时长选择确定按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['课程介绍输入框']).send_keys(description)
        EleManage().located_by_xpath(self.driver, self.ele['课程图片选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程图片选择确定按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课确定按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_perclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教课按钮']).click()
        time.sleep(0.5)
        # EleManage().located_by_xpath(self.driver, self.ele['编辑私教课课程名输入框']).clear()
        # EleManage().located_by_xpath(self.driver, self.ele['编辑私教课课程名输入框']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教课按钮保存按钮']).click()
        time.sleep(1)
        return self.driver

    def C_add_percoach(self, price):
        time.sleep(0.5)
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['添加私教课教练按钮'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课教练按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课教练课程单价输入框']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课教练带课教练选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课教练带课教练选择确定按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['添加私教课教练确定按钮']).click()
        time.sleep(1)
        return self.driver

    def D_edit_percoach(self, price):
        time.sleep(0.5)
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['编辑私教课带课教练按钮'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

        EleManage().located_by_xpath(self.driver, self.ele['编辑私教课带课教练按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教课带课教练课程单价输入框']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教课带课教练课程单价输入框']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教课带课教练确定按钮']).click()
        time.sleep(1)
        return self.driver

    def E_buy_perclass(self, end_date, price, description, phone):
        time.sleep(0.5)
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['私教课购买按钮'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        EleManage().located_by_xpath(self.driver, self.ele['私教课购买按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['失效日期输入框']).send_keys(end_date)
        EleManage().located_by_xpath(self.driver, self.ele['实付金额输入框']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['购买备注输入框']).send_keys(description)
        EleManage().located_by_xpath(self.driver, self.ele['下一步按钮1']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机输入框']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机搜索按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['私教课购买确认购买按钮']).click()
        time.sleep(1)
        return self.driver

    def F_delete_percoach(self):
        time.sleep(0.5)
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['删除私教课带课教练按钮'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        EleManage().located_by_xpath(self.driver, self.ele['删除私教课带课教练按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除私教课带课教练确定按钮']).click()
        time.sleep(1)
        return self.driver

    def G_delete_perclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除私教课按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除私教课确定按钮']).click()
        time.sleep(1)
        return self.driver
