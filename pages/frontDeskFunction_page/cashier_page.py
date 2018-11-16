import time
from public.ele_manage import EleManage


class CashierPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.ele = EleManage().cashier_page()

    def A_add_goods(self, code, name, price):
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['添加商品']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['商品条码']).send_keys(code)
        EleManage().located_by_xpath(self.driver, self.ele['商品名称']).send_keys(name)
        EleManage().located_by_xpath(self.driver, self.ele['出售单价']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['添加商品确定']).click()
        time.sleep(1)
        return self.driver

    def B_edit_goods(self, price):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑商品']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['编辑商品商品单价']).clear()
        EleManage().located_by_xpath(self.driver, self.ele['编辑商品商品单价']).send_keys(price)
        EleManage().located_by_xpath(self.driver, self.ele['编辑商品确定']).click()
        time.sleep(1)
        return self.driver

    def C_goods_entry(self):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['入库商品']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['下一步1']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['入库商品确定入库']).click()
        time.sleep(1)
        return self.driver

    def D_add_goods_entry(self, code):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['入库记录tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['商品入库按钮']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['商品条码输入框']).send_keys(code)
        EleManage().located_by_xpath(self.driver, self.ele['商品条码搜索图标']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['下一步2']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['确认入库按钮']).click()
        time.sleep(1)
        return self.driver

    def E_buy_goods(self, code):
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['快速购物tab']).click()
        time.sleep(1)
        EleManage().located_by_xpath(self.driver, self.ele['购物商品条码输入框']).send_keys(code)
        EleManage().located_by_xpath(self.driver, self.ele['购物商品条码搜索图标']).click()
        time.sleep(0.5)
        EleManage().located_by_xpath(self.driver, self.ele['现金']).click()
        EleManage().located_by_xpath(self.driver, self.ele['确认收款']).click()
        time.sleep(1)
        return self.driver



