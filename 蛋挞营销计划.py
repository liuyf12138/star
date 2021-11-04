'''
三个蛋挞师傅，制作蛋挞数目达到500个时，等待3秒再制作，工资 = 蛋挞数量 * 12
6个客人，没人有3000元，都买蛋挞，当蛋挞数量不够时，等待3秒，再次购买直到没钱

师傅类：
    属性：师傅姓名、制作蛋挞数量、工资
    操作：制作蛋挞
客人类：
    属性：客人姓名、购买蛋挞数量、余额
    操作：买蛋挞
店家类：
    属性：
        蛋挞制作数量：
        售卖蛋挞数量：
        销售金额：
        蛋挞成本：
        盈利：
    操作：
        打印盈利
'''
from threading import  Thread
import time
count = 0
# 子类继承多线程
class Cooker(Thread):

    cooker_name = ""
    cooker_num = 0
    cooker_money = cooker_num * 12

    # 子类重写run方法
    def run(self) -> None:
        global count
        while True:
            if count < 500:
                self.cooker_num = self.cooker_num + 1
                count = self.cooker_num
                self.cooker_money = self.cooker_num * 12
                print("目前",self.cooker_name,"制作蛋挞数量",self.cooker_num,"个，预计得到工资",self.cooker_money,"元","篮子里蛋挞的数量为",count)
            else:
                time.sleep(3)
                break
c1 = Cooker()
c2 = Cooker()
c3 = Cooker()
c1.cooker_name = "蔡文姬"
c2.cooker_name = "米莱迪"
c3.cooker_name = "澜"
# start方法启动多线程，并执行任务
c1.start()
c2.start()
c3.start()
# 子类继承多线程
class Custmor(Thread):
    custmor_name = ""
    custmor_num = 0
    custor_money = 3000

    # 子类重写run方法
    def run(self) -> None:
        global count
        while True:
            if count > 0:
                if self.custor_money > 0:
                    self.custmor_num = self.custmor_num + 1
                    count = self.custmor_num - 1
                    self.custor_money = self.custor_money - 3
                    print("目前",self.custmor_name,"购买蛋挞数量为",self.custmor_num,"还有",self.custor_money,"元可以买蛋挞")
                else:
                    print("店家制作的蛋挞数量为：",(self.custmor_num * 6 + 500),'\n',"售卖蛋挞数量为：",(self.custmor_num * 6),'\n',"销售金额为：",(self.custmor_num * 3 * 6),'\n',"发放工资为：",((self.custmor_num * 6 + 500) * 12),'\n',"店家盈利为：",(self.custmor_num * 3 * 6 - ((self.custmor_num * 6 + 500) * 12)))
                    break
            else:
                time.sleep(3)
                break





cc1 = Custmor()
cc2 = Custmor()
cc3 = Custmor()
cc4 = Custmor()
cc5 = Custmor()
cc6 = Custmor()
cc1.custmor_name = "杨戬"
cc2.custmor_name = "阿轲"
cc3.custmor_name = "貂蝉"
cc4.custmor_name = "程咬金"
cc5.custmor_name = "典韦"
cc6.custmor_name = "苏烈"
# start方法启动多线程，并执行任务
cc1.start()
cc2.start()
cc3.start()
cc4.start()
cc5.start()
cc6.start()
