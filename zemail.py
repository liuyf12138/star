import zmail

# 读取html里面的内容
file = open("计算器.html","r",encoding="utf-8")
msg = file.read()

# 邮件内容
msg_content = {
    "subject":"刘一凡发给你的邮件",
    "content_html":msg,
    "attachments":r"D:\python自动化测试\自动化\python\day1LYF\计算器.html"

}

# 收件人
receivers = ["2431320433@qq.com"]

# 发件人
sender = {
    "username":"luckygirl12138@163.com",
    "password":"LSRBNEIJJWZYCXCJ"
}

# 发送邮件
server = zmail.server(sender['username'],sender['password'])  #登录邮箱

server.send_mail(receivers,msg_content)

print("邮件发送成功")