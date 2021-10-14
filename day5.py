'''
 Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条
任务：打折：随机获得优惠券（9折10，5折5，1折2，面单1.
            单个商品打折9折10，5折5，1折2，面单1）

'''
import  random
#商品
shop = [["神兵小将",600],["果宝特攻",580],["虹猫蓝兔七侠传",1500],["中华小子",2500],["小福贵",5500],["天上掉下个猪八戒",3000],["大话西游",4500],["铁臂阿童木",6700],["名侦探柯南",800]]
# 获取可用余额
count = random.randint(0,8000)
print("您的可用余额为：",count)
#购物车
mycart = []
#优惠卷张数
# prices = [["9折",5],["3折"],3],["1折",1]
count1 = 0
count2 = 0
count3 = 0

while True:
    # 展示商品
    for index,value in enumerate(shop):
        print(index,"：",value)
    #抽取优惠卷
    zhe = random.randint(1,11)
    if zhe == 9:
        count1 += 1
        if count1 <=4:
            print("恭喜您获取",zhe,"折·优惠卷")
        else:
            zhe = 10
            print("您的优惠卷已使用完毕！")
    elif zhe == 5:
        count2 += 1
        if count2 <=2:
            print("恭喜您获取",zhe,"折·优惠卷")
        else:
            zhe = 10
            print("您的优惠卷已使用完毕！")
    elif zhe == 1:
        count3 += 1
        if count3 <= 0:
            print("恭喜您获取",zhe,"折·优惠卷")
        else:
            zhe = 10
            print("您的优惠卷已使用完毕！")
    else :
        zhe == 10
        print("很遗憾您未抽中优惠卷！")

    #将某件商品加入购物车
    chose = input("请输入商品编号：")
    if chose.isdigit():
        chose = int(chose)
        if chose <= len(shop):

            if count >= shop[chose-1][1] * zhe * 0.1:
                mycart.append(shop[chose-1])
                count -= shop[chose - 1][1] * zhe * 0.1
                print("该商品已加入购物车,", mycart, '\n' "您的可用余额为：", count)
            else:
                print("您的余额不足以支付该商品！")

        else:
            print("没有该商品")

    elif chose == 'q' or chose == 'Q':
        print("=======================")
        for index,value in enumerate(mycart):
            print(index,":",value)
        print("您的可用余额为：",count)
    else:
        print("请输入数值！")






