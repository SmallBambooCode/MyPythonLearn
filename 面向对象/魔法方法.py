# # __new__
# class CapStr(str):  # 父类是str
#     def __new__(cls, string):  # 重写str老祖宗的__new__方法
#         string = string.upper()
#         return super().__new__(cls, string)  # 搞完事情返回老祖宗的__new__方法
#
#
# teststr = CapStr("www.SmallBamboo.cn")
# print(teststr)

# # __add__&__radd__
# class S(str):
#     def __add__(self, other):
#         return len(self) + len(other)
#
#     def __radd__(self, other):
#         return len(other) + len(self)
#
#
# s = S("Hello")
# print(s + "World")
# print("Jerry" + s)


# # __index__
# class C:
#     def __index__(self):
#         print("__index__被拦截咯！返回个3叭~")
#         return 3
#
#
# c = C()
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l[c])

# class C:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#
# c = C("我", 18)
# # 检测对象是否有某个属性
# print(hasattr(c, "name"))
# # 获取对象属性的值
# print(getattr(c, "name"))
# print(getattr(c, "_C__age"))
# # 设置对象属性的值
# setattr(c, "_C__age", 20)
# print(getattr(c, "_C__age"))
# # 删除对象属性
# delattr(c, "name")
# print(hasattr(c, "name"))

# class C:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     def __getattribute__(self, name):
#         print("__getattribute__被拦截咯")
#         return super().__getattribute__(name)
#
#
# c = C("我", 18)
# # 获取对象属性的值
# print(getattr(c, "name"))
# print(c._C__age)

# class D:
#     def __setattr__(self, name, value):
#         # 字典键值对
#         self.__dict__[name] = value
#
#     def __delattr__(self, name):
#         del self.__dict__[name]
#
#
# d = D()
# d.name = "啊？"
# print(d.name)
# del d.name
# print(d.__dict__)

# __getitem__
# class C:
#     def __getitem__(self, index):
#         print(index)
#
#
# c = C()
# print(c[2])
# print(c[2:8])
# # 索引的实现是依靠slice函数
# s = "Hello World"
# print(s[6:])
# print(s[slice(6, None)])
# print(s[::2])
# print(s[slice(None, None, 2)])

# __setitem__
# class D:
#     def __init__(self, data):
#         self.data = data
#
#     def __getitem__(self, index):
#         print("自定义的__getitem__发挥作用咯")
#         return self.data[index]
#
#     def __setitem__(self, index, value):
#         self.data[index] = value
#
#
# d = D([1, 2, 3, 4, 5])
# print(d[1])
# print(d[2:4])
# print(d[::2])

# __iter__&__next__
# class Double:
#     def __init__(self, start, stop):
#         self.value = start - 1
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value * 2
#
#
# d = Double(1, 5)
# for i in d:
#     print(i, end=" ")

# __contains__
# class C:
#     def __init__(self, data):
#         self.data = data
#
#     def __contains__(self, item):
#         print("已调用自定义的__contains__")
#         return item in self.data
#
#
# c = C([1, 2, 3, 4, 5])
# print(3 in c)
# print(6 in c)
# print(1 not in c)

# 代偿
# class C:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         print("Iter", end=" -> ")
#         self.i = 0
#         return self
#
#     def __next__(self):
#         print("Next", end=" -> ")
#         if self.i == len(self.data):
#             raise StopIteration
#         item = self.data[self.i]
#         self.i += 1
#         return item
#
#
# c = C([1, 2, 3, 4, 5])
# print(3 in c)

# __bool__
# class D:
#     def __bool__(self):
#         print("已调用自定义的__bool__")
#         return True
#
#
# d = D()
# print(bool(d))

# 比较相关
# class S(str):
#     def __lt__(self, other):
#         return len(self) < len(other)
#
#     def __gt__(self, other):
#         return len(self) > len(other)
#
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#
# s1 = S("Hello World")
# s2 = S("Good Morning")
# s3 = S("RenAI GaGa Run!")
# print(s1 > s2)
# print(s1 < s2)
# print(s1 == s2)
# print(s1 > s3)
# print(s1 < s3)

# __call__
# class C:
#     def __call__(self, *args, **kwargs):
#         print(f"位置参数：{args}，关键字参数：{kwargs}")
#         print("疯狂打call！")
#
#
# c = C()
# c(1, 2, 3, 4, x=123, y=456)

# class Power:
#     def __init__(self, exp):
#         self.exp = exp
#
#     def __call__(self, base):
#         return base ** self.exp
#
#
# square = Power(2)
# cube = Power(3)
# print(square(1), square(2), square(3))
# print(cube(1), cube(2), cube(3))

# __str__&__repr__
class C:
    def __repr__(self):
        return "SmallBamboo"


c = C()
print(repr(c))
print(str(c))
