# # 改进我们的小游戏
# import random
#
# counts = 3
# ans = random.randint(1,10)
# while counts > 0:
#     temp = input("猜猜我是多少：")
#     guess = int(temp)
#     if guess == ans:
#         print("猜对啦")
#         break
#     else:
#         if guess > ans:
#             print("猜大了")
#         else:
#             print("猜小了")
#     counts = counts - 1
#
# print("Game Over!")

# class Check:
#     def __init__(self, cls):
#         self.cls = cls
#
#     def __call__(self, *args, **kwargs):
#         self.obj = self.cls(*args, **kwargs)
#         return self
#
#     def __getattr__(self, name):
#         print(f"正在访问{name}")
#         return getattr(self.obj, name)
#
#
# @Check
# class C:
#     def say_hi(self):
#         print("Hi~")
#
#     def say_goodbye(self):
#         print("Goodbye~")
#
#
# c = C()
# c.say_hi()
# c.say_goodbye()

import sys

print("当前 Python 版本为:", sys.version)
print("%.3f" % 30 + "%")
