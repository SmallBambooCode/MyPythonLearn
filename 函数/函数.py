# def myfunc():
#     print("Action.")
#     print("Go.")
#
# myfunc()

# def myfunc(name="Unknown"):  # 参数默认值"Unknown"
#     print("Welcome {}".format(name))
#     print("Have a nice day!")
#
#
#
# myfunc()
# myfunc("Jerry")

# def my_sum(a=0, b=0):
#     return a+b
#
#
# print(my_sum())
# print(my_sum(1, 1))

# def myfunc(a=0, b=0):
#     return a+b, a-b
#
#
# x, y = myfunc(b=1, a=5)
# print(x, y)

# def myfunc(*args, name):
#     print("有{}个参数".format(len(args)))
#     print(args)
#     print(name)
#
#
# myfunc(1, "好好好", 3, name="Jerry")

# def myfunc(a, b, c):
#     print(a, b, c)
#
#
# t = (1, 3, 5)
# myfunc(*t)

# x = 10086
#
#
# def myfunc():
#     global x
#     print(x)
#     x = 10010
#
#
# myfunc()
# print(x)

# def funA():
#     x = 10086
#     def funB():
#         x = 10010
#         print(str(x) + "In funB")
#
#
#     funB()
#     print(str(x) + "In funA")
#
#
# funA()  # 直接调用funA()不会直接调用funA()中定义的funB()，在A中手动调用B才可以

# def funA():
#     x = 10086
#     def funB():
#         nonlocal x
#         x = 10010
#         print(str(x) + "In funB")
#
#
#     funB()
#     print(str(x) + "In funA")
#
#
# funA()

def funA():
    x = 10086
    def funB():
        x = 10010
        print(str(x) + "In funB")


    print(str(x) + "In funA")
    return funB


funB_saved = funA()
funB_saved()
funB_saved()
funB_saved()
