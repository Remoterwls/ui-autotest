import time
from public.ele_manage import EleManage


class PerClassBuyPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().perclassbuy_manage()

    def A_buy_perclass(self, end_date, price, description, phone):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加购买按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程名称选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程名称选择确定按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['教练姓名选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['教练姓名选择确定按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['失效日期输入框']).send_keys(end_date)
        EleManage().located_by_xpath(self.driver, self.ele['实付金额输入框']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['购买备注输入框']).send_keys(description)
        EleManage().located_by_xpath(self.driver, self.ele['下一步按钮1']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机输入框']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机搜索按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['私教购买确定购买按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_perclass(self, description):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教购买信息按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教购买信息购买备注输入框']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教购买信息购买备注输入框']).send_keys(description)
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑私教购买信息确认修改按钮']).click()
        time.sleep(1)
        return self.driver

    def C_delete_perclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除私教购买信息按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除私教购买信息确定按钮']).click()
        time.sleep(1)
        return self.driver

