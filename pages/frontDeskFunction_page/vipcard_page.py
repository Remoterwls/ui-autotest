import time
from public.ele_manage import EleManage


class VipCard(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().vipcardmanage_page()

    def A_edit_limitcard(self, remark):
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡编辑']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡编辑备注']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['时效卡编辑备注']).send_keys(remark)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡编辑确定']).click()
        time.sleep(1)
        return self.driver

    def B_renew_limitcard(self, days):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡续卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['增加天数']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['增加天数']).send_keys(days)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡续卡确定']).click()
        time.sleep(1)
        return self.driver

    def C_passon_limitcard(self, money, phone):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡转卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡转卡实付金额']).send_keys(money)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡转卡-手机号']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡转卡-搜索图标']).click()
        EleManage().located_by_xpath(self.driver, self.ele['时效卡转卡确定']).click()
        time.sleep(1)
        return self.driver

    def D_stop_limitcard(self, start_date, end_date, money):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡停卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['停卡开始日期']).send_keys(start_date)
        EleManage().located_by_xpath(self.driver, self.ele['停卡结束日期']).send_keys(end_date)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡停卡实付金额']).send_keys(money)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡停卡确定']).click()
        time.sleep(1)
        return self.driver

    def E_delete_limitcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡删除']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡删除确定']).click()
        time.sleep(1)
        return self.driver

    def F_activate_limitcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡未开卡tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡未开卡-开卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡未开卡-开卡确定']).click()
        time.sleep(1)
        return self.driver

    def G_remove_limitcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站-更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站-删除']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站-删除确定']).click()
        time.sleep(1)
        return self.driver

    def H_recover_limitcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站-更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站-恢复']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['时效卡回收站-恢复确定']).click()
        time.sleep(1)
        return self.driver

    # 次卡
    def I_edit_countcard(self, remark):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['次卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡编辑']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡编辑备注']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['次卡编辑备注']).send_keys(remark)
        EleManage().located_by_xpath(self.driver, self.ele['次卡编辑确定']).click()
        time.sleep(1)
        return self.driver

    def J_renew_countcard(self, times):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡续卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡续卡增加次数']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['次卡续卡增加次数']).send_keys(times)
        EleManage().located_by_xpath(self.driver, self.ele['次卡续卡确定']).click()
        time.sleep(1)
        return self.driver

    def K_takeout_countcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡扣次']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡扣次确定']).click()
        time.sleep(1)
        return self.driver

    def L_passon_countcard(self, money, phone):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡转卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡转卡实付金额']).send_keys(money)
        EleManage().located_by_xpath(self.driver, self.ele['次卡转卡-手机号']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['次卡转卡-搜索图标']).click()
        EleManage().located_by_xpath(self.driver, self.ele['次卡转卡确定']).click()
        time.sleep(1)
        return self.driver

    def M_delete_countcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡删除']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡删除确定']).click()
        time.sleep(1)
        return self.driver

    def N_activate_countcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡未开卡tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['次卡未开卡-开卡']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡未开卡-开卡确定']).click()
        time.sleep(1)
        return self.driver

    def O_remove_countcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站-更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站-删除']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站-删除确定']).click()
        time.sleep(1)
        return self.driver

    def P_recover_countcard(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站-更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站-恢复']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['次卡回收站-恢复确定']).click()
        time.sleep(1)
        return self.driver
