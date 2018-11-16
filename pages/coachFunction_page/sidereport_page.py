from public.ele_manage import EleManage
import time


class SideReportPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().sidereport_manage()

    def A_add_sideReport(self, phone, side_time, age, height, weight, other):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['体侧录入按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机号输入框']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机号搜索按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['下一步按钮1']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['体侧时间输入框']).send_keys(side_time)
        EleManage().located_by_xpath(self.driver, self.ele['体侧时间确定按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['年龄']).send_keys(age)
        EleManage().located_by_xpath(self.driver, self.ele['身高']).send_keys(height)
        EleManage().located_by_xpath(self.driver, self.ele['体重']).send_keys(weight)
        EleManage().located_by_xpath(self.driver, self.ele['蛋白质']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['基础代谢']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['水分']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['体脂率']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['内脏脂肪']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['骨量']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['皮下脂肪']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['骨骼肌']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['静态心率']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['腰臀比']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['体侧录入确认按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_sideReport(self, other):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑年龄输入框']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑年龄输入框']).send_keys(other)
        EleManage().located_by_xpath(self.driver, self.ele['编辑保存按钮']).click()
        time.sleep(1)
        return self.driver

    def C_look_sideReport(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['查看按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['app查看']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['app查看关闭按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['查看按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['pc查看']).click()
        current_handle = self.driver.current_window_handle   # 此时当前窗口句柄为主窗口
        self.driver.switch_to.window(current_handle)
        # self.driver.close()
        time.sleep(1)
        return self.driver

    def D_delete_sideReport(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除确认按钮']).click()
        time.sleep(1)
        return self.driver


