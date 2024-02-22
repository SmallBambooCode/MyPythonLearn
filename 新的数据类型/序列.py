# print([1, 2, 3] + [4, 5, 6])
# print((1, 2, 3) + (4, 5, 6))
# print("1, 2, 3, " + "4, 5, 6")
# print([1, 2, 3] * 3)

# # 增量赋值和is | in | is not | not in
# s2 = s = [1, 2, 3]
# s *= 2
# print(s is s2)
# t2 = t = (1, 2, 3)
# t *= 2
# print(t is not t2)
# print(1 in s)
# print(5 not in s)
# print("我的钱" in "我的钱包")

# 使用del删除序列中的指定对象
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del x[0:4]  # 左闭右开
print(x)
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del y[::2]
# y[::2] = [] 错误的
print(y)
del y[:]
# 相当于y.clear()
print(y)
