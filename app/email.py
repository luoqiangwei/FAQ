from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#输入Email地址和口令
from_addr = "followalice@163.com"
password = "w6132197320315"
#输入SMTP服务器地址
smtp_server = "smtp.163.com"

def sendEmail(to_addr, username, vcode):
    #创建邮件对象 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative
    msg = MIMEMultipart("alternative")
    msg["From"] = _format_addr("followalice <%s>" % from_addr)
    msg["To"] = _format_addr(username + " <%s>" % to_addr) 
    msg["Subject"] = Header("FAQ 的激活邮件", "utf-8").encode()

    msg.attach(MIMEText("访问该链接激活:<br>http://127.0.0.1:8000/action?email=" + to_addr + "&vcode=" + vcode, "html", "utf-8"))

    server = smtplib.SMTP(smtp_server, 25) #SMTP地址和端口
    # ssl加密通道
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()