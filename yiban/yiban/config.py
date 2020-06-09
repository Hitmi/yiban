# 手机号-密码
ACCOUNT = 'xxx'
PASSWD = 'xxx'

# 近几天的一次易班打卡登记表的转发审批表单的链接
# 需要替换此链
with open("../config.txt") as f:
    url = f.read()

# 配置第三方 SMTP 服务
MAIL_HOST = "smtp.xxx.com"  # 设置服务器
MAIL_USER = "xx"  # 用户名
MAIL_PASS = "xxxxxx"  # 授权密码

SENDER = 'xxx@xx.com'  # 发件人
RECEIVERS = 'xxx@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


