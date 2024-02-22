# # 普通创建
# s = {"Python", "C", "C++"}
# print(s)

# # 集合推导式
# s = {x for x in "SmallBamboo"}
# # 每次打印的顺序都不一样
# print(s)

# # 类型构造器
# s2 = set("SmallBamboo25565")
# print(s2)

# # 迭代访问
# for each in s:
#     print(each, end=" ")
# print()
# print("迭代访问的顺序也是无序的")

# s = {"Python", "C", "C++"}
# print("C" in s)
# print("Java" not in s)
#
# # 使用集合对其他容器进行去重
# l = [1, 1, 4, 5, 1, 4]
# print(set(l))
# # 检测容器中的元素是否是唯一的
# print(len(l) == len(set(l)))

# s = set("SmallBamboo")
# # isdisjoint()方法判断两个集合是否不相交
# print(s.isdisjoint("GG"))
# print(s.isdisjoint(set("LittleBamboo")))
# print(s.isdisjoint("LittleBamboo"))
# # 判断对象集合是否为另一个集合的子集
# print(s.issubset("SmallBamboo.cn"))
# # 判断对象集合是否为另一个集合的超集（另一个集合是不是对象集合的子集）
# print(s.issuperset("Bamboo"))

a = {1, 2, 5, 6, 7}
b = {1, 3, 4, 5, 8}
# 并集 - 支持多参数
print(a.union(b))
print(a.union(b, {9, 10}))
# 交集 - 支持多参数
print(a.intersection(b))
# 差集（存在于对象集合而不在于另一个集合的元素） - 支持多参数
print(a.difference(b))
print(a.difference(b, {2, 6}))
# 求对称差集（并集中去掉交集）
print(a.symmetric_difference(b))
