# # 字典的创建 左键右值
# x = {"Name":"Jerry", "Age":"19"}
# y = dict(Name="Jerry", Age="19")
# z = dict([("Name", "Jerry"), ("Age", "19")])
# a = dict({"Name":"Jerry", "Age":"19"})
# b = dict({"Name":"Jerry"}, Age="19")
# c = dict(zip(["Name", "Age"], ["Jerry", "19"]))
# print(x == y == z == a == b == c)
# # 根据键找值
# print(x["Name"])
# # 新建键值对
# x["Sex"] = "Male"
# print(x)

# # 增删改查
# # 增
# # fromkeys()函数将第一个参数（可迭代对象）当作键，将第二个参数当作所有键的值
# d = dict.fromkeys("SmallBamboo", 12345)
# # 由于字典的键是唯一的，所以建完的字典键是SmalBbo
# # 对于不存在的键，新增键值对
# d["!"] = 6789
# # 对于已存在的键，修改值
# d["S"] = 6789
# print(d)
# # pop()函数可以通过键来删除键值对，
# # 当不存在时抛出异常（或者加个参数用于当作键不存在时的返回值）
# d.pop("!")
# print(d)
# d["!"] = 6789
# d.popitem()
# print(d)
# # 使用del关键字删除指定键的键值对
# del d["o"]
# print(d)
# # 使用clear()方法清空字典
# d.clear()
# print(d)
# # 删除整个字典
# del d

# d = dict.fromkeys("SmallBamboo", 12345)
# print(d)
# # 指定键，修改值
# d["S"] = 6789
# print(d)
# # 批量修改（若键不存在，则新建）
# d.update({"S": 6789, "m": "10JQK", "!": "12345"})
# d.update(a="A12")
# print(d)

# # 查
# d = dict.fromkeys("SmallBamboo", 12345)
# # 最简单的查找方式
# print(d["S"])
# # 安全的查找（使用get()方法，第二个参数是无对于键时的返回值）
# print(d.get("o", 0))
# print(d.get("Z", None))
# # 使用setdefault函数可以实现相似效果
# print(d.setdefault("S", 12345))
# print(d.setdefault("Z", None))
# items()，keys()，values()用来获取键值对，键，值
# print(d.items())
# print(d.keys())
# print(d.values())
# d.pop("b")
# print("=====AFTER=====")
# print(d.items())
# print(d.keys())
# print(d.values())

import copy
d = dict.fromkeys("SmallBamboo", 12345)
# 浅拷贝
a = d.copy()
# a = copy.copy(d)也可
# 深拷贝
b = copy.deepcopy(d)
# 验证
print(id(d))
print(id(a))
print(id(b))
