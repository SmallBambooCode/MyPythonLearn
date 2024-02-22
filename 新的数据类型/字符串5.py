# # 格式化字符串
# date = 20240214
# print("今天是"+str(date))  # 老方法
# print("今天是{}".format(date))  # 格式化字符串
# print("{} + {} = {}".format(1, 1, 2))
# print("{}看到{}就很激动".format("小学弟", "大学姐"))
# # 花括号中填入索引值，可以指定后方的参数顺序
# print("{1}看到{0}就很激动".format("小学弟", "大学姐"))
# print("{0}{1}{0}{1}{1}{0}{1}".format("F ", "T "))
# # 花括号中填入关键字
# print("{username}:{action}！".format(username="Jerry", action="登陆成功"))

# print("{:^10}".format(250))
# print("{:>5}{:<5}".format(114, 514))
# print("{:010}".format(114))  # 与C里面的printf("%010d", 114);相同
# print("{:@<5}".format(-114))

# # 加正负符号
# print("{:+} {:-}".format(10010, -10086))
# print("{: } {: }".format(10010, -10086))
# # 设置千分位分隔符
# print("{:,}".format(10010))
# # 限制小数位 浮点数：f/F为保留几位小数，g/G为保留几位有效数字
# # 非数字类型：限定最大字段的大小
# print("{:.3f}".format(1.010086))
# print("{:.3g}".format(1.010086))
# print("{:.10}".format("www.google.com"))

# # 指定输出数据格式
# print("{:b}".format(1024))  # 二进制输出
# print("{:c}".format(1024))  # 输出unicode
# print("{:d}".format(1024))  # 十进制输出
# print("{:o}".format(1024))  # 八进制输出
# print("{:#x}".format(1024))  # 十六进制输出，使用#可以加进制前缀
# print("{:#b}".format(1024))  # 二进制输出，使用#可以加进制前缀
# print("{:e}".format(1024))  # 科学计数法输出
# print("{:.4f}".format(1024))  # 浮点数输出并指定保留4位小数
# print("{:.{p}f}".format(1024, p=2))  # 浮点数输出并指定保留4位小数+套娃

# f-string
date = "2024年2月14日"
time = "21点54分"
print(f"现在是{date} {time}")
print(f"{1} + {1} = {1+1}")
# 使用刚刚学习的语法，内容需写在冒号的左边
print(f"{114514114514:,}")
p = 2
print(f"{1024:.{p}f}")
