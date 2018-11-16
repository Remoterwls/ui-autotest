import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from public.read_cfg import ReadCfg
import os


class SendEmail(object):

    def __init__(self):
        self.mail_host = ReadCfg().get_send_email_info()['mail_sever']
        self.mail_port = ReadCfg().get_send_email_info()['port']
        self.mail_account = ReadCfg().get_send_email_info()['account']
        self.mail_pwd = ReadCfg().get_send_email_info()['pwd']
        self.mail_sender = ReadCfg().get_send_email_info()['sender']
        self.mail_receiver = ReadCfg().get_send_email_info()['receiver']
        self.test_report = self.get_filepath()

    def get_filepath(self):
        # 获取上一级目录
        parent_path = os.path.dirname(os.path.dirname(__file__))
        # 定位到目录 interfaceTest\report
        test_report = parent_path + '/report'
        return test_report

    def get_filename(self):
        lists = os.listdir(self.test_report)  # 列出目录的下所有文件和文件夹保存到lists
        # print(lists)
        lists.sort(key=lambda fn: os.path.getmtime(self.test_report + "\\" + fn))  # 按时间排序
        file_name = os.path.join(self.test_report, lists[-1])  # 获取最新的文件保存到file_new
        print(file_name)
        return file_name

    def send_report(self):
        # 获取实例化对象
        message = MIMEMultipart()
        # 邮件主题
        subject = 'UI自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')
        message["from"] = self.mail_sender
        message["to"] = self.mail_receiver
        # 邮件正文有三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message.attach(MIMEText('最新测试报告如下：', 'plain', 'utf-8'))
        # 构造附件
        att = MIMEText(open(self.get_filename(), 'rb').read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename=interface_report.html'
        message.attach(att)
        try:
            mail_service = smtplib.SMTP_SSL(self.mail_host, self.mail_port)
            mail_service.login(self.mail_account, self.mail_pwd)
            mail_service.sendmail(self.mail_sender, self.mail_receiver, message.as_string())
            mail_service.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('邮件发送失败,reason is %s' % e)


if __name__ == "__main__":
    SendEmail().send_report()
