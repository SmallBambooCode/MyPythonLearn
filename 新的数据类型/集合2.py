
# s = {1, 2, 3, 5, 7, 9}
# print(s)
# # update()的方法支持多参数输入
# s.update([4, 6, 1], {10, 8})
# print(s)
# # 单纯加一个元素
# s.add("45")
# print(s)
# # 删除元素

# s = {1, 2, 3, 5, 7, 9}
# print(s)
# # remove()和discard()都可以删除一个元素
# # remove()在遇到无对应元素时会抛出异常，而discard()会静默处理
# s.remove(9)
# s.discard(8)
# s.discard(7)
# print(s)
# # 清空集合
# s.clear()
# print(s)

# t = frozenset("SmallBamboo")
# print(t)

# print(hash(1))
# print(hash(1.0000))
# print(hash(1.0000000000001))
# print(hash("2023AI"))

# fs = frozenset([1, 2, 3])
# print(fs)
# s = {fs, 4, 5, 6}
# print(s)

import copy
s = {1, 2, 3, 4, 5, 6}
t = s.copy()
t2 = copy.copy(s)
t3 = copy.deepcopy(s)
print(id(s))
print(id(t))
print(id(t2))
print(id(t3))
