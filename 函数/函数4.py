# def exchange(dollar: float, rate: float = 6.32):
#     """
#     功能：汇率转换，USD->CNY
#     参数：
#     - dollar 美元金额
#     - rate 汇率，默认6.32
#     返回值：
#     - 人民币金额
#     """
#     return dollar * rate
#
#
# # 获取函数名字
# print(exchange.__name__)
# # 获取函数类型注释
# print(exchange.__annotations__)
# # 获取函数文档
# print(exchange.__doc__)

# def exchange(dollar: float, rate: float = 6.32):
#     """
#     功能：汇率转换，USD->CNY
#     参数：
#     - dollar 美元金额
#     - rate 汇率，默认6.32
#     返回值：
#     - 人民币金额
#     """
#     return dollar * rate
#
#
# print(help(exchange))

# # 高阶函数
# import functools
#
#
# def add(x, y):
#     return x + y
#
#
# print(functools.reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# # 相当于
# print(add(9, add(8, add(7, add(6, add(5, add(4, add(3, add(2, 1)))))))))

# import functools
#
#
# # 偏函数
# def add(x, y):
#     return x + y
#
#
# add_ten = functools.partial(add, 10)
# print(add_ten(10))
# print(add_ten(90))

import time
import functools


def time_master(func):
    @functools.wraps(func)
    def call_func():
        print("Program Started")
        start = time.time()
        func()
        stop = time.time()
        print("Program Ended\n" + "Total Time: " + str(stop - start) + "s")
    return call_func


@time_master
def myfunc():
    time.sleep(2)
    print("Hello")


myfunc()
print(myfunc.__name__)