# class C:
#     def __init__(self):
#         self._x = 250
#
#     def getx(self):
#         return self._x
#
#     def setx(self, x):
#         self._x = x
#
#     def delx(self):
#         del self._x
#
#     # 指定了属性的获取、设置和删除方法
#     x = property(getx, setx, delx)
#
#
# c = C()
# print(c.x)
# c.x = 500  # 调用property指定的setx方法
# print(c.x)  # 调用property指定的getx方法
# del c.x  # 调用property指定的delx方法
# print(c.__dict__)

# class C:
#     def __init__(self):
#         self._x = 250
#
#     def __getattr__(self, name):
#         if name == 'x':
#             return self._x
#         else:
#             super().__getattribute__(name)
#
#     def __setattr__(self, name, value):
#         if name == 'x':
#             super().__setattr__('_x', value)
#         else:
#             super().__setattr__(name, value)
#
#     def __delattr__(self, name):
#         if name == 'x':
#             super().__delattr__('_x')
#         else:
#             super().__delattr__(name)
#
#
# c = C()
# print(c.x)
# c.x = 500
# print(c.x)
# del c.x
# print(c.__dict__)

# class E:
#     def __init__(self):
#         self._x = 250
#
#     @property
#     def x(self):
#         return self._x
#
#     # x = property(x)，这里的装饰器相当于这句代码
#     # 只传入了第一个参数，所以不支持写入和删除（只读属性）
#
# e = E()
# print(e.x)
# e.x = 500  # 此处报错
# print(e.x)

class E:
    def __init__(self):
        self._x = 250

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


e = E()
print(e.x)
e.x = 500
print(e.x)
del e.x
print(e.__dict__)
