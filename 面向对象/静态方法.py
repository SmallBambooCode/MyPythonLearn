# class C:
#     @staticmethod
#     def funC():
#         print("我是静态方法")
#
#
# c1 = C()
# c1.funC()
# C.funC()

class C:
    count = 0

    def __init__(self):
        C.count += 1

    @staticmethod
    def get_count():
        print(f"该类一共实例化了{C.count}个对象")


c1 = C()
c2 = C()
c3 = C()
c3.get_count()
