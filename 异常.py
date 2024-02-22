# 以下全是引发异常的代码
# print(1 / 0)
# print(“Hello World”)
# print("Love" + 520)

# try:
#     print(1 / 0)
#     print("啊？" + 10086)
# # 捕获多个指定的异常
# except (ZeroDivisionError, ValueError, TypeError) as e:
#     # pass：占位符，不执行任何操作
#     pass
# print("doge")

# try:
#     print("正常输出" + str(10086))
# except:
#     print("有异常了！")
# else:
#     print("没有异常。")

# try:
#     print("正常输出" + str(10086))
#     # print("{}".format(1/0))
# except:
#     print("有异常了！")
# else:
#     print("没有异常！")
# finally:
#     print("Done.")

# try:
#     try:
#         print("150" + 150)
#     except:
#         print("inner error!")
#     print(1 / 0)
# except:
#     print("outer error!")
# finally:
#     print("Done.")

try:
    s = "Hello World"
    assert s != "Hello World"
except AssertionError as e:
    print("已引发AssertionError")

# # 异常链
# try:
#     try:
#         print(1 / 0)
#
#     except ZeroDivisionError as e:
#         raise ValueError("啥玩意，值不对！") from e
# except ValueError as e2:
#     print(e2)
