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

class MetaC(type):
    def __call__(cls, *args, **kwargs):
        print("__call__() in MetaC")


class C(metaclass=MetaC):
    pass


c = C()
