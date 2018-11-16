import time
from public.ele_manage import EleManage


class PerOrderPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().perclassorder_manage()

    def A_order_perclass(self, phone):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加预约按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机号输入框']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机号搜索按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['上课时间选择按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['确认预约按钮']).click()
        time.sleep(1)
        return self.driver

    def B_finish_perclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['消课按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['确认无误，开始消课按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['消课取消按钮']).click()
        time.sleep(1)
        return self.driver

    def C_cancel_perclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['取消预约按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['取消预约确定按钮']).click()
        time.sleep(1)
        return self.driver
