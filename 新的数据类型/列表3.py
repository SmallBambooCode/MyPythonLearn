# 列表推导式

# # 循环实现
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x)
# for i in range(len(x)):
#     x[i] = x[i] * 2
# print(x)

# # 列表推导式实现
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(x)
# x = [i * 2 for i in x]
# print(x)

# # numpy
# import numpy
# x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(x)
# x = x * 2
# print(x)


# x = [i for i in range(10)]
# print(x)
# x = [i + 1 for i in range(10)]
# print(x)

# # 将嵌套列表中的每个列表的第二个元素取出
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# z = [y[1] for y in x]
# print(z)

# # 将嵌套列表中的"对角线"取出
# x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# z = [x[y][y] for y in range(len(x))]
# print(z)

# # 使用列表推导式解决嵌套列表的坑
# x = [[0] * 3 for i in range(3)]
# print(x)
# x[1][1] = 1
# print(x)

# # 加入if分句
# x = [i + 1 for i in range(30) if (i + 1) % 2 == 0]
# print(x)

# # 列表推导式的嵌套
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# x = [col for row in matrix for col in row]
# print(matrix)
# print(x)

# 终极列表推导式语法
x = [[x, y] for x in range(10) if x % 2 == 0 for y in range(10) if y % 3 == 0]
print(x)
# 同理
z = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 3 == 0:
                z.append([x, y])
print(z)
