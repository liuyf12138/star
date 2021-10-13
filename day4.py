#输入字符成为值，按照顺序默认成为健
# name = input("请输入字符:")
# dict = {}
# for i,x in zip(range(1,len(name)+1),name):
#     dict[i] = x
#     print(dict)

#将嵌套字典里所有值输出
dict = {"a1":"1","a2":"2","a3":{"b1":"3","b2":"4","b3":{"c1":"5","c2":"6","c3":{"d1":"7","d2":"8"}}}}
# in_dict:需要处理的字典, target_key:目标键
# value:输出的列表,元素为目标键值对应的值(必须为空列表), not_ldt:获取的目标类型不为dict
# for k,v in dict.items():
#         print('\n',k,end=': ')
#         for x,y in v.items():
#             print(x,y,end=' ')
#
# def get_dict_value(in_dict, target_key, results=[], not_d=True):
#     for key in in_dict.keys():  # 迭代当前的字典层级
#         data = in_dict[key]  # 将当前字典层级的第一个元素的值赋值给data
#
#         # 如果当前data属于dict类型, 进行回归
#         if isinstance(data, dict):
#             get_dict_value(data, target_key, results=results, not_d=not_d)
#
#         # 如果当前键与目标键相等, 并且判断是否要筛选
#         if key == target_key and isinstance(data, dict) != not_d:
#             results.append(in_dict[key])
#
#     return results



#任务一：统计每个人的平均薪资、平均年龄、将新来员工添加到列表中、男女人数、每个部门人数
# names = [["曹操","56","男","106","IBM",500,"50"],
#          ["大乔","19","女","230","微软",501,"60"],
#          ["小乔","19","女","210","Oracle",600,"60"],
#          ["许诸","45","男","230","Tencent",700,"10"]
#          ]
# avgmoney = int((names[0][5]+names[1][5]+names[2][5]+names[3][5])) / 4
# avgage =  int(int(names[0][1])+int(names[1][1])+int(names[2][1])+int(names[3][1])) / 4
# names.append(["刘备","45","男","220","alibaba",500,"30"])
# print(names)
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0
# count6 = 0
# for i in range(0,5):
#
#     if names[i][2] == "男":
#         count1 += 1
#
#     elif names[i][2] == "女":
#         count2 += 1
# for i in range(0, 5):
#
#     if names[i][6] == "10":
#         count3 += 1
#     elif names[i][6] == "30":
#         count4 += 1
#     elif names[i][6] == "50":
#         count5 += 1
#     elif names[i][6] == "60":
#         count6 += 1
# print('每个人平均工资为：%d' %(avgmoney))
# print('每个人平均年龄为： %d' %(avgage))
# print("公司男人数为：",count1)
# print("公司女人数为：",count2)
# print("公司部门“10”人数为：",count3)
# print("公司部门“30”人数为：",count4)
# print("公司部门“50”人数为：",count5)
# print("公司部门“60”人数为：",count6)

#任务二：现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
#[罗恩, 23 ,35 ,44]
#[哈利 ,60, 77 ,68 ,88, 90]
#[赫敏, 97 ,99 ,89 ,91, 95, 90]
#[马尔福 ,100, 85 ,90]
#求每个人的总成绩
# scores = [["罗恩", 23 ,35 ,44],["哈利" ,60, 77 ,68 ,88, 90],["赫敏", 97 ,99 ,89 ,91, 95, 90],["马尔福" ,100, 85 ,90]]
# luoen = int(scores[0][1] + scores[0][2] + scores[0][3])
# hary = int(scores[1][1] + scores[1][2] + scores[1][3] +scores[1][4] + scores[1][5])
# hemin = int(scores[2][1] + scores[2][2] + scores[2][3] +scores[2][4] + scores[2][5] +scores[2][6])
# maerfu = int(scores[3][1] + scores[3][2] + scores[3][3])
# print("罗恩、哈利、赫敏、马尔福的总成绩分别为：",luoen,hary,hemin,maerfu)


#当输入54321时，输出结果为：1 2 3 4 5
# num = int(input("请输入一个数："))
# while num != 0:
#     print(num % 10)
#     num = num // 10

#冒泡排序
a = [5,2,4,7,9,1,3,5,4,0,6,1,3]
#默认升序排序
a.sort()

print(a)
#降序排序
a.sort(reverse = True)
print(a)