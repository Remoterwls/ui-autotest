from public.ele_manage import EleManage
import time
import os


class PassageManage(object):

    def __init__(self, driver):
        self.ele = EleManage().passage_manage()
        self.driver = driver

    def A_add_passage(self, title, abstract, content):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['添加文章按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['文章名称输入框']).send_keys(title)
        self.driver.find_element_by_xpath(self.ele['文章封面上传按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['文章封面上传弹窗按钮']).click()
        os.system(r'C:\Users\Administrator\UI\testFile\upfile\IMG002.exe')
        self.driver.find_element_by_xpath(self.ele['文章封面保存按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['文章摘要输入框']).send_keys(abstract)
        # 进入iframe
        frame = self.driver.find_element_by_class_name(self.ele['文章摘要输入框iframe'])
        self.driver.switch_to.frame(frame)
        self.driver.find_element_by_xpath(self.ele['文章内容输入框']).send_keys(content)
        # 退出iframe
        self.driver.switch_to.default_content()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['添加文章确定按钮']).click()
        time.sleep(1)
        return self.driver

    def B_edit_passage(self, title):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['编辑文章按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['文章名称输入框']).clear()
        self.driver.find_element_by_xpath(self.ele['文章名称输入框']).send_keys(title)
        self.driver.find_element_by_xpath(self.ele['编辑文章提交按钮']).click()
        time.sleep(1)
        return self.driver

    def C_search_passage(self, title):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['文章标题搜索输入框']).send_keys(title)
        self.driver.find_element_by_xpath(self.ele['文章标题搜索图标']).click()
        time.sleep(1)
        return self.driver

    def D_del_passage(self):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['删除文章按钮']).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(self.ele['删除文章确定按钮']).click()
        time.sleep(1)
        return self.driver










