# d = dict.fromkeys("SmallBamboo", 12345)
# # 使用len()求键值对数量
# print(len(d))
# # 使用in，not in判断键是否在字典中
# print("S" in d)
# print("D" not in d)
# # 字典中的键值对，键，值也可以转为列表
# print(list(d.items()))
# print(list(d.keys()))  # 相当于list(d)
# print(list(d.values()))
# # iter()函数，将字典的键构成迭代器
# e = iter(d)
# # 使用next()取出迭代器中的一个元素
# print(next(e), end=" ")
# # 使用for循环遍历迭代器
# for i in e:
#     print(i, end=" ")
# print()
# print(d.keys())
# print(sorted(d))
# print(sorted(d, reverse=True))

# # 字典嵌套字典
# d = {"Jerry": {"计算编程思维": "96", "计算机科学导论": "96"}, "Danny": {"计算编程思维": "94", "计算机科学导论": "99"}}
# print(d)
# print(d["Danny"])
# print(d["Danny"]["计算编程思维"])
# # 字典嵌套列表（当然也可以嵌套其他序列）
# dl = {"Jerry": [96, 96], "Danny": [94, 99]}
# print(dl)
# print(dl["Danny"])
# print(dl["Danny"][0])

# 字典推导式
d = {'S':70, 'm':105, 'B':115, 'o':104}
# 反转键值
b = {v:k for k,v in d.items()}
print(d)
print(b)
c = {v:k for k,v in d.items() if v > 100}
print(c)
# 求字符ASCII码示例
d = {ch:ord(ch) for ch in "AaBbCcDd"}
print(d)
d = {x:y for x in [1, 3, 5] for y in [2, 4, 6]}
print(d)
