# def myfunc1():
#     print("调用myfunc1()")
#
#
# def myfunc2():
#     print("调用myfunc2()")
#
#
# def report(func):
#     print("调用开始")
#     func()
#     print("调用完成")
#
#
# report(myfunc1)
# report = report(myfunc2)

# import time
# def time_master(func):
#     print("Program Started")
#     start = time.time()
#     func()
#     stop = time.time()
#     print("Program Ended\n" + "Total Time: " + str(stop - start) + "s")
#
#
# def myfunc():
#     time.sleep(2)
#     print("Hello")
#
#
# time_master(myfunc)


# import time
# def time_master(func):
#     def call_func():
#         print("Program Started")
#         start = time.time()
#         func()
#         stop = time.time()
#         print("Program Ended\n" + "Total Time: " + str(stop - start) + "s")
#     return call_func
#
# @time_master
# def myfunc():
#     time.sleep(2)
#     print("Hello")
#
#
# myfunc()

# def add(func):
#     def inner():
#         x = func()
#         return x + 1
#     return inner
#
#
# def cube(func):
#     def inner():
#         x = func()
#         return pow(x, 3)
#     return inner
#
#
# def square(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
#
# @add
# @cube
# @square
# def mytest():
#     return 2
#
#
# print(mytest())

# 传递多个参数
import time
def logger(msg):
    def time_master(func):
        def call_func():
            print("Program {} Started".format(msg))
            start = time.time()
            func()
            stop = time.time()
            print("Program Ended\n" + "Total Time: " + str(stop - start) + "s")
        return call_func
    return time_master


@logger("myfunc函数")
def myfunc():
    time.sleep(2)
    print("Hello")


@logger("myfunc2函数")
def myfunc2():
    time.sleep(2)
    print("Bye Bye")

myfunc()
myfunc2()
