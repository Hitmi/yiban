import json

from yiban import yb
from yiban.config import url
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def parse_data(url):
    """
    :param url
    将分享链接的数据解析出来生成表单数据字典
    """
    initiateId = url.split('=')[-1]
    # print(initiateId)
    share_url = 'https://api.uyiban.com/workFlow/c/share/index?InitiateId={}&CSRF={}'.format(initiateId, yb.CSRF)
    share_res = yb.request(share_url, cookies=yb.COOKIES)
    save_data_url = share_res.get('data')['uri']
    save_data_res = requests.get(save_data_url)
    save_data = save_data_res.json()
    FormDataJson = save_data.get('Initiate')['FormDataJson']
    dict_form = {i.get('id'): i.get("value") for i in FormDataJson}
    return json.dumps(dict_form)


def send_email(mail_host, mail_user, mail_pass, sender, receiver, subject, coontent):
    '''
    :param mail_host: 设置服务器
    :param mail_user: 用户名
    :param mail_pass: 授权密码
    :param sender: 邮件发送者
    :param receivers: 邮件接收者
    :param subject: 邮件主题
    :param coontent: 邮件主题
    :return: true
    '''
    # 配置第三方 SMTP 服务
    mail_host = mail_host  # 设置服务器
    mail_user = mail_user  # 用户名
    mail_pass = mail_pass  # 口令

    sender = sender

    message = MIMEText(coontent, 'plain', 'utf-8')

    message['from'] = sender
    message['to'] = receiver
    subject = subject
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    return True


# 最终提交的表单数据
form_data = parse_data(url)

if __name__ == '__main__':
    # 打印表单提取的数据
    print(json.loads(form_data))
