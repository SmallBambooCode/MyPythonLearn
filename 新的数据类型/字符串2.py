# # 查找
# x = "lava: Hello World"
# # 计数（可指定start和end参数，注意这个范围是左闭右开区间）
# print(x.count("l", 8, len(x)))
# # 从左往右找到下
# print(x.find("l", 0, len(x)))  # 若找不到返回-1
# print(x.index("l"))  # 若找不到则抛出异常
# # 从右往左找到下标
# print(x.rfind("l", 0, len(x)))  # 若找不到返回-1
# print(x.rindex("l"))  # 若找不到则抛出异常

# 替换
# # tab变空格，默认为1tab=8space，如需自定义可以输入参数
# code = """
# \tprint("This is a tab")
#     print("This is some spaces")"""
# print(code)
# print(code.expandtabs())
# print(code.expandtabs(4))

# # 替换指定的字符串，并指定替换次数，-1且默认为无限制
# x = "I love Python and Python loves me."
# print(x.replace("Python", "Jetbrains", 1))
# print(x.replace("Python", "Jetbrains"))

# 按照转换表进行替换
x = "I love Python and Python loves me."
myTable = str.maketrans("ne", "#E")
print(x.translate(myTable))
# maketrans的第三个参数用于忽略指定的字符串，例如"love"
print(x.translate(str.maketrans("ne", "#E", "love")))
