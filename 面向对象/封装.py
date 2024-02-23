# # "私有变量"
# class C:
#     def __init__(self, x):
#         self.__x = x
#
#     def set_x(self, x):
#         self.__x = x
#
#     def get_x(self):
#         return self.__x
#
# c = C(10086)
# print(c.get_x())
# c.set_x(10010)
# print(c.__dict__)
# print(c._C__x)

# __slots__类属性

class C:
    __slots__ = ["a", "b", "c"]

    def __init__(self, a, b):
        self.a = a
        self.b = b


c = C(1, 5)
c.c = 9
print(c.a, c.b, c.c)
