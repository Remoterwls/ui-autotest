import configparser
from os import path


""" 通过当前目录定位cfg.ini的文件位置"""
parent_path = path.dirname(path.dirname(__file__))
final_path = path.join(parent_path, "testFile\cfg.ini")
# print(final_path)


class ReadCfg(object):
    """ 读取cfg.ini文件，返回各个参数值构成的字典"""

    def __init__(self):
        self.cof = configparser.ConfigParser()
        self.cof.read(final_path, encoding='utf-8')

    def get_login_account_info(self):
        login_account = dict()
        login_account['登录账号'] = self.cof.get('LoginAccount', 'username')
        login_account['登录密码'] = self.cof.get('LoginAccount', 'password')
        return login_account

    def get_login_url_info(self):
        login_url = dict()
        login_url['登录url'] = self.cof.get('LoginUrl', 'url')
        return login_url

    def get_send_email_info(self):
        send_email = dict()
        send_email['发件服务器'] = self.cof.get('SendEmail', 'mail_sever')
        send_email['端口号'] = self.cof.get('SendEmail', 'port')
        send_email['邮件账户名'] = self.cof.get('SendEmail', 'account')
        send_email['邮件密码'] = self.cof.get('SendEmail', 'pwd')
        send_email['发件人'] = self.cof.get('SendEmail', 'sender')
        send_email['收件人'] = self.cof.get('SendEmail', 'receiver')
        return send_email


if __name__ == "__main__":
    A = ReadCfg()
    a = A.get_login_account_info()
    b = A.get_login_url_info()
    c = A.get_send_email_info()
    print(a, b, c)




