import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import base64
from importlib.machinery import SourceFileLoader

conf = SourceFileLoader("config","./config/config.py").load_module()



#附件添加
def  messsges(filename):
    file = filename.split("/")
    date = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    date["Content-Type"] = 'application/octet-stream'
    date["Content-Disposition"] = 'attachment; filename=%s' % file[-1]
    return date

#授权码解密
def  get_pass(password):
    ha = "FZamsyTkd"
    tu = base64.b64decode(base64.b64decode(password.encode()).decode().replace(ha,"").encode()).decode()
    return tu




def send_msg(message, send_men):

    try:
        for k in [send_men]:
            #初始化邮件对象
            msg=MIMEMultipart()
            #添加邮件内容
            msg.attach(MIMEText(message, 'plain', 'utf-8'))
            #添加邮件发送者
            msg['From']=formataddr([conf.send_user,conf.send_user])
            #添加邮件接收者
            msg['To']=formataddr([k,k])
            #添加邮件title
            msg['Subject']= conf.send_title
            #添加邮件附件
            for mm in conf.file_path_list:
                msg.attach(messsges(mm))
            server=smtplib.SMTP_SSL(conf.mail_server_ip, conf.mail_server_port)
            server.login(conf.send_user, get_pass(conf.send_pass))
            server.sendmail(conf.send_user, [k,], msg.as_string())
            server.quit()
            print("接收者:%s 邮件发送成功!"%k)
    except Exception as f:
        print("邮件发送失败%s"%f)

