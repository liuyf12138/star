# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

'''# 用户输入华氏温度
fsd=float(input("请输入华氏温度："))
# 计算摄氏温度
ssd = 5.0/9*(fsd - 32)
# 输出华氏度转化成摄氏度的结果
print('%0.1f 华氏温度转化为摄氏温度为： %0.1f' %(fsd,ssd))'''

'''# 练习2：输入圆的半径计算计算周长和面积。
# 用户输入圆的半径
r = float(input("请输入半径："))
# 计算圆的周长
zc = 2 * 3.14 * r
# 计算圆的面积
mj = 3.14 * r * r
# 输出结果
print('%0.1f 圆的周长为： %0.1f' %(r,zc))
print('%0.1f 圆的面积为： %0.1f' %(r,mj))'''

# 练习3：输入年份判断是不是闰年。

# while True:
# # 用户输入年份
#     year = int(input("请输入年份："))
# # 判断是否为闰年
#     if year % 4 == 0 & year % 100 != 0:
#         print(year, "为闰年")
#
#
#     elif year % 400 == 0:
#         print(year, "为闰年")
#
#     else:
#         print(year, "不是闰年")




# # 练习4：英制单位英寸与公制单位厘米互换。
# # 提示：需要键盘输入长度，需要键盘输入单位
# while True:
#     # 用户输入长度
#     length = float(input("请输入长度:"))
#     # 用户输入单位
#     dw = input("请输入单位：")
#     # 英寸转换成厘米
#     inch = 2.54 * length
#
#     # 判断转换成英制单位英寸还是公制单位厘米
#     if dw == "英寸":
#         # 厘米转换成英寸
#         centimeter = 2.54 * length
#
#         print('%0.1f 英寸 英寸转换为厘米为： %0.1f 厘米' %(length,centimeter))
#     elif dw == "厘米":
#         # 英寸转换成厘米
#         inch = length / 2.54
#         print('%0.1f 厘米 厘米转换为英寸为： %0.1f 英寸' % (length, inch))
#     else:
#         print("输入格式不正确，请重新输入！")
#         break

# 练习5：百分制成绩转换为等级制成绩。
# 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
# 70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。   **0.5
# while True:
#     # 用户输入成绩
#     score = float(input("请输入成绩："))
#     score1 = int(score)
#     # 判断成绩对应等级
#     if score1 >= 90:
#         print("A")
#     elif score1 >= 80 and score1 < 90:
#         print("B")
#     elif score1 >= 70 and score1 < 80:
#         print("C")
#
#
#     elif score1 >= 60 and score1 < 70:
#         print("D")
#     else:
#         print("E")

# 练习6：输入三条边长，如果能构成三角形就计算周长和面积
# 提示：需要手动输入三条边长
while True:
    # 用户输入边长a
    sidea = float(input("请输入边长a："))
    # 用户输入边长b
    sideb = float(input("请输入边长b："))
    # 用户输入边长c
    sidec = float(input("请输入边长c："))
    # 判断是否构成三角形
    if sidea + sideb > sidec and sidea + sidec > sideb and sideb + sidec > sidea:
        length = sidea+sideb+sidec
        phl = 1.0/2 * length
        area = (phl-sidea)*(phl-sideb)*(phl-sidec)**0.5
        print('%0.1f %0.1f %0.1f 构成三角形的周长为：%.1f' %(sidea,sideb,sidec,length))
        print('%0.1f %0.1f %0.1f 构成三角形的面积为：%.1f' % (sidea, sideb, sidec, area))
        print(type(length))
        print(type(area))
    else:
        print("不能构成三角形，请重新输入边长！")

