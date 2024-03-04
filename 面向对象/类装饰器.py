# def report(cls):
#     def oncall(*args, **kwargs):
#         print("开始实例化对象")
#         _ = cls(*args, **kwargs)
#         print("实例化完成")
#         return _
#     return oncall
#
#
# @report
# # 相当于C = report(C)
# class C:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         print("C:__init__")
#
#
# c = C(1, 2, 3)

# class Counter:
#     def __init__(self, func):
#         self.count = 0
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(f"Counter.__call__已被调用{self.count}次")
#         return self.func(*args, **kwargs)
#
#
# @Counter
# def say_hi():
#     print("Hi~")
#
#
# say_hi()
# say_hi()

def report(cls):
    class Check:
        def __init__(self, *args, **kwargs):
            self.obj = cls(*args, **kwargs)

        def __getattr__(self, name):
            print(f"正在访问{name}")
            return getattr(self.obj, name)
    return Check


@report
class C:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"{self.name}, Hi~")

    def say_goodbye(self):
        print(f"{self.name}, Goodbye~")


c1 = C("Jerry")
c2 = C("Danny")
c1.say_hi()
c1.say_goodbye()
c2.say_hi()
