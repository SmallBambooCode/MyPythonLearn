# squareY = lambda y: y * y
# print(squareY(10))
# y = [lambda x: x* x, 2, 3]
# print(y[0](y[1]))
# print(y[0](y[2]))
# # 使用映射map()
# mapped = map(lambda x: ord(x) + 10, "SmallBamboo")
# print(list(mapped))
# # 使用过滤器filter()
# filtered = filter(lambda x: x % 2, range(10))
# print(list(filtered))

# # 生成器
# def counter():
#     i = 0
#     while i <= 5:
#         yield i
#         i += 1
#
#
# gen = counter()
# # 支持next()函数
# print(next(gen))
# print(next(gen))
# print("=")
# for each in gen:
#     print(each)

# # 斐波那契数列示例
# def fib():
#     a, b = 0, 1
#     while 1:
#         yield a
#         a, b = b, b + a
#
#
# f = fib()
# for i in range(20):
#     if i % 5 == 0 and i != 0:
#         print()
#     print(next(f), end=" ")

# t = (i1 + i2 for i1 in range(3) for i2 in range(4,7))
# for each in t:
#     print(each, end=" ")

# # 递归实现阶乘
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))

# 汉诺塔
def hanoi(n, x, y, z):
    if n == 1:
        print(x, "->", z)
    else:
        hanoi(n-1, x, z, y)
        print(x, "->", z)
        hanoi(n-1, y, x, z)


n = int(input())
hanoi(n, "A", "B", "C")
