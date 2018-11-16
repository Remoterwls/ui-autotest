import time
from public.ele_manage import EleManage


class GroupClassPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele1 = EleManage().meun_manage()
        self.ele = EleManage().groupclass_manage()

    def A_add_groupclass(self, name, price, address, min_num, max_num):
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['添加课程按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程类型选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程类型选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['教练姓名选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['教练姓名选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['课程名称输入框']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['课程价格输入框']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['上课地点']).send_keys(address)
        EleManage().located_by_xpath(self.driver, self.ele['最少人数']).send_keys(min_num)
        EleManage().located_by_xpath(self.driver, self.ele['最多人数']).send_keys(max_num)
        EleManage().located_by_xpath(self.driver, self.ele['添加课程确定按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_groupclass(self, name):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程课程名称输入框']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程课程名称输入框']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['编辑课程确定']).click()
        time.sleep(1)
        return self.driver

    def C_queuing_groupclass(self, start_date, end_date, start_time, end_time):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['排期']).click()
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['排期确定'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        EleManage().located_by_xpath(self.driver, self.ele['开始日期']).send_keys(start_date)
        EleManage().located_by_xpath(self.driver, self.ele['结束日期']).send_keys(end_date)
        # 点击空白
        EleManage().located_by_xpath(self.driver, '//*[@id="pane-3-4-2"]/div/div[5]/div/div[2]/div/div[3]/span[2]').click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['团课课程排期周日选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['开始时间']).send_keys(start_time)
        EleManage().located_by_xpath(self.driver, self.ele['结束时间']).send_keys(end_time)
        EleManage().located_by_xpath(self.driver, self.ele['排期确定']).click()
        time.sleep(1)
        return self.driver

    def D_delete_groupclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除课程']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除课程确定']).click()
        time.sleep(1)
        return self.driver

    def E_add_queuing(self, start_date, end_date, start_time, end_time):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程排期tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['添加排期']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加已有课程tab']).click()
        EleManage().located_by_xpath(self.driver, self.ele['课程选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['课程选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['添加排期开始日期']).send_keys(start_date)
        EleManage().located_by_xpath(self.driver, self.ele['添加排期结束日期']).send_keys(end_date)
        EleManage().located_by_xpath(self.driver, '//*[@id="pane-3-4-1"]/div/div[3]/div/div[2]/div/div[3]/span[2]').click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加排期周日选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['添加排期开始时间']).send_keys(start_time)
        EleManage().located_by_xpath(self.driver, self.ele['添加排期结束时间']).send_keys(end_time)
        EleManage().located_by_xpath(self.driver, self.ele['添加排期确定']).click()
        time.sleep(1)
        return self.driver

    def F_edit_queuing(self, end_time):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['周日选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑排期']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑排期结束时间']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑排期结束时间']).send_keys(end_time)
        EleManage().located_by_xpath(self.driver, self.ele['编辑排期确定']).click()
        time.sleep(1)
        return self.driver

    def G_order_class(self, price, phone):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['周日选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['预约课程']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['实付金额']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['下一步1']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员手机号']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['搜索图标']).click()
        EleManage().located_by_xpath(self.driver, self.ele['确认预约按钮']).click()
        time.sleep(1)
        return self.driver

    def H_cancel_class(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['周日选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['查看预约']).click()
        # 操作下拉滚动条方法，直到指定元素可见
        target = self.driver.find_element_by_xpath(self.ele['取消预约'])
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['取消预约']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['取消预约确定']).click()
        time.sleep(1)
        return self.driver

    def I_delete_queuing(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['周日选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除排期']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['删除排期确定']).click()
        time.sleep(1)
        return self.driver

    def J_print_groupclass(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['打印课表']).click()
        time.sleep(1)
        return self.driver
