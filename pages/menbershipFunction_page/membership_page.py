from public.ele_manage import EleManage
import time


class MemberShipPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().membership_manage()

    def A_add_potential_customers(self, name, phone, remark):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客登记']).click()
        EleManage().located_by_xpath(self.driver, self.ele['姓名']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['性别选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['性别选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['手机号']).send_keys(phone)
        EleManage().located_by_xpath(self.driver, self.ele['会籍选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会籍选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['来源选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['来源选择确定']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['意向选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['意向选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['目的选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['目的选择确定']).click()
        EleManage().located_by_xpath(self.driver, self.ele['备注']).send_keys(remark)
        EleManage().located_by_xpath(self.driver, self.ele['潜客登记提交按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_potential_customers(self, birth):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客编辑']).click()
        EleManage().located_by_xpath(self.driver, self.ele['潜客编辑生日']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['潜客编辑生日']).send_keys(birth)
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客编辑确定']).click()
        time.sleep(1)
        return self.driver

    def C_distribute_member(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客分配会籍']).click()
        EleManage().located_by_xpath(self.driver, self.ele['分配会籍选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['分配会籍选择确定']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客分配会籍确定按钮']).click()
        time.sleep(2)
        return self.driver

    def D_distribute_coach(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客分配教练']).click()
        EleManage().located_by_xpath(self.driver, self.ele['分配教练选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['分配教练选择确定']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客分配教练确定按钮']).click()
        time.sleep(1)
        return self.driver

    def E_delete_potential_customers(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客删除']).click()
        EleManage().located_by_xpath(self.driver, self.ele['潜客删除确定']).click()
        time.sleep(1)
        return self.driver

    def F_recovery_potential_customers(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客回收站tab']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['潜客恢复']).click()
        EleManage().located_by_xpath(self.driver, self.ele['潜客恢复确定']).click()
        time.sleep(1)
        return self.driver

    def G_edit_vip(self, birth):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理tab']).click()
        time.sleep(1)   # 切换tab至少sleep 1s
        EleManage().located_by_xpath(self.driver, self.ele['会员管理更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理编辑']).click()
        EleManage().located_by_xpath(self.driver, self.ele['会员管理编辑生日']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['会员管理编辑生日']).send_keys(birth)
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理编辑确定']).click()
        time.sleep(1)
        return self.driver

    def H_distribute_vipmember(self):
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理分配会籍']).click()
        EleManage().located_by_xpath(self.driver, self.ele['分配会籍-选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['分配会籍-选择确定']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理分配会籍确定按钮']).click()
        time.sleep(1)
        return self.driver

    def I_distribute_vipcoach(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理分配教练']).click()
        EleManage().located_by_xpath(self.driver, self.ele['分配教练-选择']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['分配教练-选择确定']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理分配教练确定按钮']).click()
        time.sleep(1)
        return self.driver

    def J_delete_vip(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理更多']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理删除']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['会员管理删除确定']).click()
        time.sleep(1)
        return self.driver




