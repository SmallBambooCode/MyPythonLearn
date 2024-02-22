# # 截取
# # 去除字符串左侧或右侧空白
# x = "      冀ICP备2023024410号-2       "
# print(x.lstrip())
# print(x.rstrip())
# # 左右留白同时去除
# print(x.strip())
# # 去除左右特定字符，加入参数
# y = "www.smallbamboo.cn"
# print(y)
# print(y.lstrip("w.cn"))
# print(y.rstrip("w.cn"))
# print(y.strip("w.cn"))
# # 去除左右指定子字符串（Python3.9+）
# # print(y.removeprefix("www."))
# # print(y.removesuffix(".cn"))

# # 拆分
# # 从左向右找分隔符，分割字符串存至三元组
# x = "www.SmallBamboo.cn"
# print(x.partition("."))
# # 从右向左找分隔符，分割字符串存至三元组
# print(x.rpartition("."))
# # 按照指定的分隔符拆分，不包含分隔符（默认切空格）
# print("11 45 14".split())
# print(x.split("."))
# # 按照指定的分隔符拆分，不包含分隔符，加入参数用于切几刀
# print(x.split(".", 1))
# print(x.rsplit(".", 1))
# # 将字符串按行分割并返回列表，兼容所有操作系统的换行方式\n，\r，\r\n
# y = "读书的女人最美丽，\n读书的女人最优秀，\r\n读书的女人最通情达理。"
# print(y.splitlines())
# # 加入参数可以指定是否把分割结果包含换行符
# print(y.splitlines(True))

# 拼接
# 以一个字符串作为分隔符，将参数（列表/元组）中的字符串用分隔符拼接并返回
x = " | "
print(x.join(["Fish", "Cake", "Milk"]))
print(".".join(("notes", "SmallBamboo", "com")))
print("".join(["SmallBamboo", "SmallBamboo", "SmallBamboo"]))
# 使用join进行字符串的拼接比加号更快
