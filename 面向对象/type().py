# class C:
#     pass
#
#
# print(type(3.1415926))
# print(str)
# print(type("好好好") == str)
# # 相当于list("R U OK?")
# print(type([250])("R U OK?"))
# print(type({}).fromkeys("HelloWorld"))
# # 重点来了！类的类型是type？
# print(type(C))
# print(type(type))
# print(type(str))

# C = type("C", (), {})
# c = C()
# print(C.__bases__)
# D = type("D", (C,), {})
# print(D.__bases__)
# E = type("E", (), dict(x=250, y=500))
# print(E.x, E.y)
#
#
# def funC(self):
#     print("好好好")
#
#
# F = type("F", (), dict(funA=funC))
# f = F()
# f.funA()

# class C:
#     def __init_subclass__(cls):
#         print("定义子类后触发：__init_subclass__")
#         cls.x = 250
#
#
# class D(C):
#     x = 500
#
#
# # 这里打印的是父类的x属性
# print(D.x)

class C:
    def __init_subclass__(cls, value):
        print("定义子类后触发：__init_subclass__")
        cls.x = value


class D(C, value=250):
    x = 500


# 这里打印的是父类的x属性
print(D.x)
# type的第四个参数
E = type("E", (C,), dict(x=500), value=250)
print(E.x)
