# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 判断所有元素是否为真
# print(all(l))
# # 判断是否存在元素为真
# print(any(l))

# l = ["Python", "C++", "JavaScript", "Java", "Go", "Typescript"]
# # enumerate()用于返回一个枚举对象
# # 将可迭代对象中的每一个元素及从0开始的序号共同构成一个二元组（两个元素组成的元组）的列表
# print(enumerate(l))
# print(list(enumerate(l)))
# # 自定义序号开始的值
# print(list(enumerate(l, 1)))

# import itertools
# l = ["Python", "C++", "JavaScript"]
# l2 = ["Java", "Go", "Typescript"]
# n = [0, 1, 2, 3]
# # zip()函数用于创建一个聚合多个可迭代对象的迭代器
# # 将传入的可迭代对象的每个元素依次组成元组
# print(list(zip(l2, l, n)))
# print(list(itertools.zip_longest(l2, l, n)))

# # map()函数会根据提供的函数对指定的可迭代对象的每一个元素进行计算，返回结果的迭代器
# print(list(map(ord, "Python")))
# # 以下代码同理
# mapped_list = []
# for ch in "Python":
#     mapped_list.append(ord(ch))
# print(mapped_list)

# print(list(map(pow, [1, 2, 3, 4], range(4))))
# # 1^0 2^1 3^2 4^3

# # filter()函数根据提供的函数对指定的可迭代对象的每个元素进行运算，以迭代器的形式返回结果为真的元素。
# print(list(filter(str.isupper, "SmallBamboo")))

# mapped = map(ord, "SmallBamboo")
# for each in mapped:
#     print(each, end=" ")
# print()
# print(list(mapped))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = iter(x)
print(type(x))
print(type(y))
# 取出迭代器中一个元素
print(next(y))
