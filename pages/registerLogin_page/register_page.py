from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, os
from public.data_generate import DataGenerate
from public.read_cfg import ReadCfg
from public.ele_manage import EleManage
from public.get_vercode import GetVercode


class RegisterPage(object):

    def __init__(self, driver):
        """准备数据"""
        self.url = ReadCfg().get_login_url_info()['登录url']
        self.phone = DataGenerate().create_phone()
        self.account = DataGenerate().create_str()
        self.pwd = DataGenerate().create_str()
        self.address = '武汉市光谷软件园'
        self.gymname = DataGenerate().create_txt()
        self.name = DataGenerate().create_txt()[0:2]
        """准备元素字典"""
        self.ele = EleManage().register_manage()
        """准备验证码"""
        self.ver_code = GetVercode().get_vercode(self.phone)
        self.driver = driver
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def register(self):
        self.driver.find_element_by_xpath(self.ele['马上注册按钮']).click()
        # 显式等待直到登录账号输入框出现
        account_ele = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, self.ele['登录账号输入框']))
        )
        account_ele.send_keys(self.account)
        self.driver.find_element_by_xpath(self.ele['登录密码输入框']).send_keys(self.pwd)
        self.driver.find_element_by_xpath(self.ele['确认密码输入框']).send_keys(self.pwd)
        self.driver.find_element_by_xpath(self.ele['场馆名称输入框']).send_keys(self.gymname)
        self.driver.find_element_by_xpath(self.ele['地址输入框']).send_keys(self.address)
        time.sleep(1)
        # 执行js，使元素变为可见状态
        js = "document.getElementById('searchResultPanel').style.display='block'"
        self.driver.execute_script(js)
        time.sleep(1)
        # 点击元素选择城市位置(这里重点注意下，先悬浮再点击)
        address_ele = self.driver.find_element_by_xpath(self.ele['选择城市具体位置'])
        ActionChains(self.driver).move_to_element(address_ele).click().perform()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele['继续按钮1']).click()
        # 显式等待直到姓名输入框出现
        name_ele = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, self.ele['法人姓名输入框']))
        )
        name_ele.send_keys(self.name)
        self.driver.find_element_by_xpath(self.ele['法人手机号输入框']).send_keys(self.phone)
        self.driver.find_element_by_xpath(self.ele['验证码输入框']).send_keys(self.ver_code)
        self.driver.find_element_by_xpath(self.ele['继续按钮2']).click()
        # # 显式等待直到LOGO上传按钮出现(无法实现)
        # WebDriverWait(self.driver, 5, 0.5).until(
        #     EC.presence_of_element_located((By.XPATH, self.ele['LOGO上传按钮']))
        # )
        time.sleep(2)
        self.driver.find_element_by_xpath(self.ele['LOGO上传按钮']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele['LOGO上传弹窗按钮']).click()
        time.sleep(1)
        os.system(r'D:\UI\testFile\LOGO001.exe')
        self.driver.find_element_by_xpath(self.ele['LOGO保存按钮']).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.ele['场馆图片上传按钮']).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.ele['场馆图片上传弹窗按钮']).click()
        time.sleep(1)
        os.system(r'D:\UI\testFile\IMG001.exe')
        self.driver.find_element_by_xpath(self.ele['场馆图片保存按钮']).click()
        self.driver.find_element_by_xpath(self.ele['场馆电话输入框']).send_keys(self.phone)
        self.driver.find_element_by_xpath(self.ele['游泳']).click()
        self.driver.find_element_by_xpath(self.ele['瑜伽']).click()
        self.driver.find_element_by_xpath(self.ele['私教']).click()
        self.driver.find_element_by_xpath(self.ele['团体操']).click()
        self.driver.find_element_by_xpath(self.ele['完成注册按钮']).click()
        time.sleep(2)  # 此处等待是为了断言
        return self.driver


if __name__ == "__main__":
    d = webdriver.Chrome()
    RegisterPage(d).register()











