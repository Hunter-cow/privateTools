# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#用法
#sender = 'huntercow@163.com'
#receivers = ['3147738347@qq.com','3371446454@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#sendEmail(sender,receivers,"测试文件","测试内容")



#四个参数 发送者 接受者 主题 消息内容
def sendEmail(sender,receivers,subject,msg):

    sendONE = sender #发送者
    receONE = '@All' #接受着
    #subject = 'Python SMTP 邮件测试'  #主题
    #msg = '发送的内容' #内容
    # 第三方 SMTP 服务 配置
    mail_host="smtp.163.com"  #设置服务器
    mail_user="Huntercow@163.com"    #用户名
    mail_pass="OVKKYGQOOQGAILUD"   #口令 

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header(sendONE, 'utf-8')   # 发送者
    message['To'] =  Header(receONE, 'utf-8')        # 接收者

    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
        return
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
        return

