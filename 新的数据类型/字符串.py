# # 大小写转换
# x = "java: Hello World"
# print(x)
# # 首字母大写，其他小写
# print(x.capitalize())
# # 所有字母小写（支持英语外的更多字符）
# print(x.casefold())
# # 每个单词首字母大写，其他小写
# print(x.title())
# # 大写小写反转
# print(x.swapcase())
# # 全部大写
# print(x.upper())
# # 全部小写
# print(x.lower())

# 左中右对齐
x = "java: Hello World"
# 居中对齐
print(x.center(len(x)+10, "#"))
# 左对齐
print(x.ljust(len(x)+10, "*"))
# 右对齐
print(x.rjust(len(x)+10, "@"))
# 用0填充左侧（用于填充时间，例如01:01和23:33可以用同一个代码实现）
h, m = "12", "5"
print(h.zfill(2)+":"+m.zfill(2))
