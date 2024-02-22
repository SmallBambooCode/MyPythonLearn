# # 列表元组字符串相互转换
# s = "Hello World"
# print(list(s))
# print(tuple(s))
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(str(l)*2)

# # 对比元素，返回最大或最小值
# s = [1, 1, 4, 5, 1, 4]
# print(str(min(s)) + " " + str(max(s)))
# t = "SmallBamboo"
# print(max(t) + " " + min(t))  # 比的是ASCII码大小
# print(max([], default=0))
# # 第二种用法：传入多个参数
# print(max(1, 5, 4, 6))
# print(min(0, 5, 4, 6))

# len和sum
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 对可迭代对象求长度（有几个元素）
print(len(l))
# 对可迭代对象求和
print(sum(l))
# 指定求和的起始值
print(sum(l, 45))

# # 排序
# s = [1, 2, 3, 0, 6]
# print(sorted(s))
# print(s)
# print(sorted(s, reverse=True))
# # 排序中的key参数
# t = ["Python", "C++", "JavaScript", "Java", "Go", "Typescript"]
# print(sorted(t))
# # 根据元素长度排序
# print(sorted(t, key=len))
# # reversed()用于返回一个反向迭代器（新的对象）
# for i in reversed(t):
#     print(i, end=' ')
# print()
# # 将反向迭代器转换为列表输出
# print(list(reversed(t)))
