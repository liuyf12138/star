import smtplib
import unittest
from email.mime.multipart import MIMEMultipart  # MIMEMulipart模块构造带附件
from email.mime.text import MIMEText  # MIMRText()定义邮件正文
from email.header import Header
from HTMLTestRunner import HTMLTestRunner

#加载所有测试用例
tests = unittest.defaultTestLoader.discover(r"D:\python自动化测试\自动化\python\day1LYF",pattern="test*.py")
#运行期执行测试用例，并生成测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="加法计算",
    verbosity=1,
    stream=open(file="计算器.html",mode="w+",encoding="utf-8")

)
#运行
runner.run(tests)
# #发送邮件的服务器（网易邮箱的发件服务器：smtp.163.com；收件服务器：pop3.163.com）
# smtpserver = "smtp.163.com"
# #发送邮件的用户和密码
# user ="luckygirl12138@163.com"
# password = "NHOZAHPWDSNJWMEN"
# #发件人
# sender = "luckygirl12138@163.com"
# #收件人
# receiver = "1244933380@qq.com"
# #主题
# subject = "计算器的测试报告"
# #附件
# sendfile = open("D:\python自动化测试\自动化\python\day1LYF\计算器.html","rb").read()
# #创建附件实例
# msgRoot = MIMEMultipart()
# msgRoot['From'] = Header("大鹏展翅",'utf-8')
# msgRoot['To'] = Header("小鸡炖蘑菇",'utf-8')
# msgRoot['Subject'] = Header(subject,'utf-8')
#
# #邮件正文内容
# msgRoot.attach(MIMEText('这是计算器的测试报告，请查收','plain','utf-8'))
# # 构造附件1，传送当前目录下的 test.txt 文件
# att = MIMEText(sendfile,'html','utf-8')
# att.add_header("Content-Type","application/octet-stream")
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att.add_header("Content-Disposition","attachment",filename = '计算器.html')
# msgRoot.attach(att)
#
# smtp = smtplib.SMTP_SSL(smtpserver,465)
# smtp.connect(smtpserver)
# smtp.login(user,password)
# smtp.sendmail(sender,receiver,msgRoot.as_string())
# smtp.quit()
# def sendemailwithfile():
#     #发送邮件的服务器
#     smtpserver = 'smtp.qq.com'
#     #发送邮件用户和密码
#     user ='599789637@qq.com'
#     password = 'hxcmgzgcvpuvbfdi'
#     #发送者
#     sender = '599789637@qq.com'
#     #接收者
#     receiver = '1244933380@qq.com'
#     #邮件主题
#     subject = "苏维嘉"
#     #发送附件
#     sendfile = open("D:\\python自动化测试\\自动化\\python\\day1LYF\\计算器.html","rb").read()
#     att = MIMEText(sendfile,"base64","utf-8")
#     att["content-type"] = "application/octet-stream"
#     # att["content-disposition"] = "attachment;filename = '计算器.html'"
#     att.add_header('Content-Disposition', 'attachment', filename='计算器.html')
#     msgroot = MIMEMultipart('related')
#     msgroot['subject'] = subject
#     msgroot.attach(att)
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(user,password)
#     smtp.sendmail(sender,receiver,msgroot.as_string())
#     smtp.quit()
# sendemailwithfile()
