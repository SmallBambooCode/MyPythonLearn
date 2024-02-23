# 类方法
# class C:
#     def funA(self):
#         print(self)
#
#     @classmethod
#     def funB(cls):
#         print(cls)
#
#
# c = C()
# print(c.funA())
# print(c.funB())

# class C:
#     count = 0
#
#     def __init__(self):
#         C.count += 1
#
#     @classmethod
#     def get_count(cls):
#         print(f"该类一共实例化了{cls.count}个对象")
#
#
# c1 = C()
# c2 = C()
# c3 = C()
# c3.get_count()

class C:
    count = 0

    @classmethod
    def add(cls):
        cls.count += 1

    def __init__(self):
        self.add()

    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了{cls.count}个对象")


class D(C):
    count = 0


class E(C):
    count = 0


c1 = C()
d1, d2 = D(), D()
e1, e2, e3 = E(), E(), E()
c1.get_count()
d1.get_count()
e1.get_count()
