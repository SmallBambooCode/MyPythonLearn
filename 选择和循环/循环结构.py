# # while循环
# t = 4
# while t:
#     print(t)
#     t = t - 1
# print("Done.")

# # 九九乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, "*", i, "=", j * i, end="\t")
#         j += 1
#     print()
#     i += 1

# # for遍历字符串
# i = 0
# for ch in "2023仁爱嘎嘎冲！":
#     i += 1
#     print(ch, end=" ")
#     if i % 4 == 0:
#         print()

# # while的相同实现
# i = 0
# while i < len("2023仁爱嘎嘎冲！"):
#     print("2023仁爱嘎嘎冲！"[i], end=" ")
#     i += 1
#     if i % 2 == 0:
#         print()

# range迭代器
for i in range(10):
    print(i, end=" ")
print()
for i in range(1, 11):
    print(i, end=" ")
print()
for i in range(1, 22, 2):
    print(i, end=" ")
