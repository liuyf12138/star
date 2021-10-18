import  random

#创建空字典，用来放置用户
bank = {}
#定义开户行
bank_name = "中国工商银行昌平支行"
#添加用户的函数
def bank_add(account,name,password,country,province,street,door):
    if name in bank:
        return 2
    elif len(bank) >= 100:
        return 3
    else:
        bank[name] = {
            "账号": account,
            "用户名": name,
            "用户密码": password,
            "国家": country,
            "省份": province,
            "街道": street,
            "门牌号": door,
            "存款": 0,
            "开户行": bank_name
        }
        return 1
#用户的详细信息函数
def user_add():
    account = random.randint(10000000,99999999)
    name = input("请输入用户名：")
    password = input("请输入用户密码：")
    print("请输入您的地址：")
    country = input("请输入国家：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入门牌号：")

    #调用bank_add函数，将输入的用户信息，添加到用户库中
    add = bank_add(account,name,password,country,province,street,door)
    if add == 3:
        print("用户库已满请到其他银行支行开户")
    elif add == 2:
        print("该用户已存在")
    elif add == 1:
        print("开户成功！")

        info = '''
            账号：%s
            用户名：%s
            密码：****
            国家：%s
            省份：%s
            街道：%s
            门牌号：%s
            存款：%s
            开户行：%s
        
            
        '''
        #每个元素都可传入%
        print(info % (account,name,country,province,street,door,bank[name]["存款"],bank_name))
#存款函数
def money_add():
    name = input("请输入用户名：")
    if name in bank:
        smoney = int(input("请输入存款额度："))

        bank[name]["存款"] += smoney
        print("=====================")
        print("您的用户名", name, "的账户存款额度为：", bank[name]["存款"])
    else:
        print("该用户不存在！")


#取钱函数
def money_sun():
    name = input("请输入用户名：")
    if name in bank:
        password = input("请输入用户密码：")
        if password == bank[name]["用户密码"]:
            sunmoney = int(input("请输入取款额度："))
            if sunmoney <= bank[name]["存款"]:
                bank[name]["存款"] -= sunmoney
                print("取款成功！您的存款为：",bank[name]["存款"])
            else:
                print("额度不支持取款！")
        else:
            print("密码不正确")
    else:
        print("该用户不存在！")
#转账
def transferMoney():
    name = input("请输入转出账户用户名：")
    if name in bank:
        inname = input("请输入转入账户用户名：")
        if inname in bank:
            password = input("请输入用户密码：")
            if password == bank[name]["用户密码"]:

                transferMoney = int(input("请输入转账金额："))
                if transferMoney <= bank[name]["存款"]:
                    bank[name]["存款"] -= transferMoney
                    print("转账成功！您的用户余额为：",bank[name]["存款"])
                    return 0
                else:
                    print("余额不足以转账！")
                    return 3
            else:
                print("密码不正确！")
                return 2


        else:
            print("转入账户不存在！")
            return 1

    else:
        print("转出账户不存在！")
        return 1
#查询
def inquiry():
    name = input("请输入用户名：")
    if name in bank:
        password = input("请输入密码：")
        if password == bank[name]["用户密码"]:
            print("当前用户为：",name,'\n',"余额为：",bank[name]["存款"],'\n',"住址为：",bank[name]["国家"],bank[name]["省份"],bank[name]["街道"],bank[name]["门牌号"],'\n',"开户行为：",bank[name]["开户行"])
        else:
            print("密码不正确！")
    else:
        print("用户不存在！")

while True:
    # 打印菜单
    print("***********************")
    print("*    中国工商银行       *")
    print("*    账户管理系统       *")
    print("***********************")
    print("* 1.添加用户            *")
    print("* 2.存钱               *")
    print("* 3.取钱               *")
    print("* 4.转账               *")
    print("* 5.查询               *")
    print("* 6.Bye!              *")
    print("***********************")
    #输入数字进入模块进行操作
    str1 = int(input("请输入要进行的操作："))
    if str1 == 1:
        print("进入添加用户界面")
        user_add()
        print(bank)

    elif str1 == 2:
        print("进入存钱界面")
        money_add()
    elif str1 == 3:
        print("进入取钱界面")
        money_sun()

    elif str1 == 4:
        print("进入转账界面")
        transferMoney()

    elif str1 == 5:
        print("进入查询界面")
        inquiry()

    elif str1 == 6:
        print("退出中国工商银行财务管理系统！")

