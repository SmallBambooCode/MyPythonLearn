# class MetaC(type):
#     pass
#
#
# # metaclass=用来指定元类
# class C(metaclass=MetaC):
#     pass
#
#
# c = C()
# print(type(c))
# print(type(C))
# print(type(MetaC))
# import types


# class MetaC(type):
#     def __new__(mcls, name, bases, attrs):
#         print("__new__() in MetaC")
#         print(f"mcls = {mcls}, bases = {bases}, attrs = {attrs}")
#         return type.__new__(mcls, name, bases, attrs)
#
#     def __init__(cls, name, bases, attrs):
#         print("__init__() in MetaC")
#         print(f"name = {name}, bases = {bases}, attrs = {attrs}")
#         type.__init__(cls, name, bases, attrs)
#
#
# class C(metaclass=MetaC):
#     def __new__(cls):
#         print("__new__() in C")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("__init__ in C")
#
#
# print("making c obj")
# c = C()

# class MetaC(type):
#     def __call__(cls, *args, **kwargs):
#         print("__call__() in MetaC")
#
#
# class C(metaclass=MetaC):
#     pass
#
#
# c = C()

# class MetaC(type):
#     def __new__(mcls, name, bases, attrs):
#         attrs['author'] = "SmallBamboo"
#         return type.__new__(mcls, name, bases, attrs)
#
#
# class C(metaclass=MetaC):
#     pass
#
#
# class D(metaclass=MetaC):
#     pass
#
#
# c = C()
# d = D()
# print(c.author)
# print(d.author)

# class MetaC(type):
#     def __init__(cls, name, bases, attrs):
#         cls.author = "SmallBamboo"
#         return type.__init__(cls, name, bases, attrs)
#
#
# class C(metaclass=MetaC):
#     pass
#
#
# class D(metaclass=MetaC):
#     pass
#
#
# c = C()
# d = D()
# print(c.author)
# print(d.author)

# class MetaC(type):
#     def __init__(cls, name, bases, attrs):
#         if not name.istitle():
#             raise TypeError("类名需大写字母开头！")
#         type.__init__(cls, name, bases, attrs)
#
#
# class Mycls:
#     pass

# class MetaC(type):
#     def __call__(cls, *args, **kwargs):
#         new_args = [each.upper() for each in args if isinstance(each, str)]
#         return type.__call__(cls, *new_args, **kwargs)
#
#
# class C(metaclass=MetaC):
#     def __init__(self, name):
#         self.name = name
#
#
# c = C("SmallBamboo")
# print(c.name)

# class MetaC(type):
#     def __call__(cls, *args, **kwargs):
#         if args:
#             raise TypeError("只支持关键字参数！")
#         return type.__call__(cls, *args, **kwargs)
#
#
# class C(metaclass=MetaC):
#     def __init__(self, name):
#         self.name = name
#
#
# c = C("SmallBamboo")

# class NoInstances(type):
#     def __call__(cls, *args, **kwargs):
#         raise TypeError("该类不允许实例化对象！")
#
#
# class C(metaclass=NoInstances):
#     @staticmethod
#     def static_ok():
#         print("staticmethod:Hello world")
#
#     @classmethod
#     def class_ok(cls):
#         print("classmethod:Hello world")
#
#
# C.static_ok()
# C.class_ok()

class SingleInstances(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        type.__init__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class C(metaclass=SingleInstances):
    pass

c1 = C()
c2 = C()
print(c1 == c2)
