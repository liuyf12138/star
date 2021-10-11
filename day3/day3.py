# -----------------
# 任务一：实现输入10个数字，并打印10个数的求和结果
# 方案一：
# while True:
#     # 输入整型a
#     a = input("请输入数字(数字之间用“,”隔开)：")
#     # 定义一个空的列表
#     b = a.split(",")
#     sum = 0
#     for i in range(0,len(b)):
#         sum +=int(b[i])
#     print(sum)

# 方案二：
# print("请输入十个数字求和")
# sumH = 0
# for i in range(10):
#     nub = input("请输入第{}个数字：".format(i+1))
#     if nub.isdigit():
#         nub = int(nub)
#         sumH = sumH + nub
#         print("ok")
#     else:
#         print("null")

#----------------------------------------
# 任务二：从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# 输入10个数
# while True:
#     # 输入整型a
#     a = input("请输入数字(数字之间用“,”隔开)：")
#     # 定义一个空的列表
#     b = a.split(",")
#     # 假设最大值是第一个，和是0，平均值是第一个
#     sum = 0
#     max = b[0]
#     avg = b[0]
#     # 判断最大值
#     for i in range(1,len(b)):
#         sum += int(b[i])
#         avg = sum / len(b)
#         if b[i] > b[i-1]:
#             max = int(b[i])
#         else:
#             max = int(b[i-1])
#     # 输出
#     print("最大值为：",max)
#     print("和为：", sum)
#     print("最大值为：", avg)


#------------------------------------------------
# 任务三：使用random模块，如何产生 50~150之间的数？
# import random
# ran = random.randint(50,151)
# print("随机产生的数为：",ran)

#-------------------
# 任务四：从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# while True:
#     sidea = int(input("请输入边长a："))
#     sideb = int(input("请输入边长b："))
#     sidec = int(input("请输入边长c："))
#     if sidea + sideb > sidec and sidea + sidec > sideb and sideb +sidec >sidea:
#
#         if sidea == sideb and sideb == sidec:
#             print("该三角形为等边三角形")
#         elif sidea == sideb and sideb != sidec or sidea == sidec and sidea != sideb or sideb == sidec and sidec != sidea:
#             print("该三角形为等腰三角形")
#         elif sidea**2 + sideb**2 == sidec**2 or sidea**2 + sidec**2 == sideb**2 or sideb**2 + sidec**2 == sidea**2:
#             print("该三角形为直角三角形")
#         else:
#             print("该三角形为普通三角形")
#     else:
#         print("不能构成三角形")

#-----------------------------------------------
#任务五：有以下两个数，使用+，-号实现两个数的调换。
# while True:
#     num1 = input("请输入第一个变量：")
#     num2 = input("请输入第二个变量：")
#     if input().split('+') or input().split('-'):
#         num3 = num2
#         num2 = num1
#         print("交换后为：",num3,num2)
#     else:
#         print("输入内容有误！")


#------------------------------------------
#任务六：实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# while True:
#     #保存用户和密码
#     import time
#     count = 0
#     username = "root"
#     userpassword = "admin"
#     close = ["root1","admin1"]
#     # 输入用户名
#     name = input("请输入用户名：")
#     if name in close:
#         print("该用户为黑名单")
#     else:
#
#         if name != username:
#             print("该用户不存在")
#         else:
#     # 输入密码
#             password = input("请输入密码：")
#             if name == username and password == userpassword:
#                 print("登录成功")
#             elif name == username and password != userpassword:
#
#                 while count < 3:
#                     if password != userpassword:
#                         print("密码不正确，请重新输入！")
#                         password = input("请再次输入密码：")
#                         count += 1
#                         if count == 2 and password != userpassword:
#                             close.append(name)
#                             print("该用户将被锁定，请稍后再重新登录！")
#                             time.sleep(60)
#
#
#                         elif count ==2 and password ==userpassword:
#                             print("登录成功")
#                             break
#                     else:
#                         print("登录成功")
#                         break

#---------------------------------------------------------------
#任务七：编程实现下列图形的打印
#三角形输出
# n = eval(input())
# for i in range(1,n+1,2):
#     print("{0:^{1}}".format("*" * i,n))
#---------------------------------------------------------------
#任务八：使用while循环实现NxN乘法表的打印
# x = int(input("请输入一个数字:"))
# while x < 10:
#     y = 1
#     while y <= x:
#         print('%s * %s = %s' %(y,x,x*y),end=' ')
#         y += 1
#     print('\n')
#     x +=1


#-------------------------------------------------------------
#任务九：编程实现99乘法表的倒叙打印
# x = 9
# while x > 0:
#     y = x
#     while y <= x and y > 0:
#         print('%s * %s = %s' % (y, x, x * y), end=' ')
#         y = y-1
#     print('\n')
#     x = x-1

#-------------------------------------------------------------------
#任务十：一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
# day = 0
# height = 20
# while height > 0 :
#     height -= 3
# #    print(height)
#     day += 1
#     if height > 0:
#         height += 2
# #        print(height)
# print("第",day,"天能出来")


#---------------------------------
#任务十一：
# 继续完成上午的猜数字游戏的需求功能。
# 1.添加计数打印功能
# 2.添加次数金币功能和锁定系统功能
# import random
# x = int(input("请输入随机范围最小值："))
# y = int(input("请输入随机范围最大值："))
# ran = random.randint(x,y)
# print(ran)
# cv = 500
# count = int(input("请输入金币娱乐次数："))
# sum = count * cv
# print("本次娱乐预计消费",sum,"个金币，游戏开始！",'\n',"友情提示:随机范围为：","(",x,y,")")
# num1 = int(input("猜一猜小艺给出的数字："))
# sum -= 500
# while count >= 0:
#     if num1 == ran:
#         count -= 1
#         sum += 1000
#         print("太棒了！你猜对啦！恭喜你获得1000个金币，本次结束后金币数量为：",sum,"可以开始下一轮游戏啦！")
#         break
#     elif num1 > ran:
#         count -= 1
#         sum -= 500
#         print("输入的数大了！")
#     elif num1 < ran:
#         count -= 1
#         sum -= 500
#         print("输入的数小了!")
#
#     num1 = int(input("继续耐心猜一猜小艺给出的数字哦！"))
#     if count == 0 and num1 != ran:
#         print("很遗憾本次金币已用完，游戏结束！")

#---------------------
#任务十二：用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
while True:
    x = int(input("请输入实现从1到多少的阶乘："))
    sum = 1
    for i in range(1,x+1):
        sum = sum * i
    print(sum)

