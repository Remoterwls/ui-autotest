from public.ele_manage import EleManage
import time


class OpenClassPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().openclass_manage()

    def A_add_openclass(self, name, address, mix_num, max_num):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加公开课按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程名称输入框']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['教练姓名选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['教练姓名选择确认按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['上课地点输入框']).send_keys(address)
        EleManage().located_by_xpath(self.driver, self.ele['上课人数最小输入框']).send_keys(mix_num)
        EleManage().located_by_xpath(self.driver, self.ele['上课人数最大输入框']).send_keys(max_num)
        EleManage().located_by_xpath(self.driver, self.ele['上课时间选择按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['周一选择确定按钮']).click()
        EleManage().located_by_xpath(self.driver, self.ele['上课开始时间输入框']).click()
        # EleManage().located_by_xpath(self.driver, self.ele['上课开始时间输入框']).send_keys(self.start_time)
        # time.sleep(1)
        # EleManage().located_by_xpath(self.driver, self.ele['上课结束时间输入框']).clear()
        # EleManage().located_by_xpath(self.driver, self.ele['上课结束时间输入框']).send_keys(self.end_time)
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['上课时间确定按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加公开课确认按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_openclass(self, name):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['选择周一课程']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程课程名称输入框']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程课程名称输入框']).send_keys(name)
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程确定按钮']).click()
        time.sleep(1)
        return self.driver

    def C_delete_openclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['选择周一课程']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除公开课按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除公开课确认按钮']).click()
        time.sleep(1)
        return self.driver

    def D_print_openclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['打印课表']).click()
        time.sleep(1)
        return self.driver



