# mylist = [1, 1, 4, 5, 1, 4]
# print(mylist)
# mylist = mylist * 3
# print(mylist)

# # 创建嵌套列表
# mylist = [[1, 1], [4, 5], [1, 4]]
# # 访问嵌套列表
# print(mylist[1][0])
# for i in mylist:
#     for j in i:
#         print(j, end=" ")
#     print()

# mylist = [[0] * 3] * 3
# print(mylist)
# mylist[1][1] = 1
# print(mylist)
# print(mylist[0] is mylist[1])
# print(mylist[0] is mylist[2])

# 我的实验
# x = [0, 1] * 2
# print(x)
# y = [x] * 2 # 此处的x为可变对象，所以乘法得到的部分为之前的引用
# print(y)
# y[0][0] = 2
# print(y)

# 实现深拷贝
import copy
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 深拷贝
y = copy.deepcopy(x)
# 浅拷贝
z = x
# z = copy.copy(x)
x[1][1] = 0
print(x)
print(y)
print(z)