# rhyme = (1, 2, 3, 4, 5, "上山打老虎")
# # rhyme = 1, 2, 3, 4, 5, "上山打老虎"
# print(rhyme)
#
# # 通过下标获取元素
# for i in range(len(rhyme)):
#     print(rhyme[i],end=" ")
# print()
#
# # 以下切片操作与列表相同
# print(rhyme[:])
# print(rhyme[:5])
# print(rhyme[::2])
#
# # 元组的“查”
# print("元组的“查”")
# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9)
# print(nums.count(9))
# print(nums.index(9))
#
# # 加法&乘法
# print("加法&乘法")
# s = (1, 2, 3)
# t = (4, 5, 6)
# print(s + t)
# print(s * 3)
# # 嵌套
# print("嵌套")
# w = s, t
# print(w)

# # 如何生成只有一个元素的元组
# x = (114514)
# y = (114514,)
# print(x)
# print(y)
# print(type(x))
# print(type(y))

# # 打包和解包
# x = (1, "2", [3])
# print(x)
# y1, y2, y3 = x
# print(y1, y2, y3)

# 关于*
z1, z2, *z3 = "Hello"
print(z1, z2, z3)
a = [1, 2, 3]
print(*a)
