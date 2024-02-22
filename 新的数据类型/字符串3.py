# # 判断
# # 判断参数指定的子字符串是否出现在字符串的起始位置（后面可以加起始和结束位置参数（左开右闭））
# x = "I love you, you love me, MIXUE Ice cream and tea"
# print(x.startswith("I"))
# print(x.startswith("I love you"))
# print(x.startswith("you love me"))
# print(x.startswith("you love me", 12, len(x)))

# # 判断参数指定的子字符串是否出现在字符串的末尾位置（后面可以加起始和结束位置参数（左开右闭））
# x = "I love you, you love me, MIXUE Ice cream and tea"
# print(x.endswith("tea"))
# print(x.endswith("Ice cream and tea"))
# print(x.endswith("MIXUE"))
# print(x.endswith("MIXUE", 0, x.rfind("MIXUE") + 5))

# # 以元组的形式传入待匹配参数
# icp = "冀ICP备2023024410号-1"
# if icp.startswith(("京", "津", "冀")):
#     print("您的域名是在京津冀备案的")
# else:
#     print("您的域名不是在京津冀备案的")
# icp = "陕ICP备2023009366号-1"
# if icp.startswith(("京", "津", "冀")):
#     print("您的域名是在京津冀备案的")
# else:
#     print("您的域名不是在京津冀备案的")

# # 判断字符串的每个单词开头是否大写，并且其余小写
# x = "I love you, you love me, MIXUE Ice cream and tea"
# print(x.istitle())
# x = "I Love You, You Love Me, Mixue Ice Cream And Tea"
# print(x.istitle())

# # 判断字符串的全部字母是否大写或小写
# x = "I love you, you love me, MIXUE Ice cream and tea"
# print(x.isupper())
# print(x.upper().isupper())
# print(x.islower())
# print(x.lower().islower())

# # 判断字符串是否仅由字母构成
# x = "I love you, you love me, MIXUE Ice cream and tea"
# print(x.isalpha())
# x = "IloveyouyoulovemeMIXUEIcecreamandtea"
# print(x.isalpha())
# # 判断字符串是否为空白字符串
# x = "   \n"
# print(x.isspace())
# # 判断字符串是否是可打印的
# x = "I love you, you love me, MIXUE Ice cream and tea"
# print(x.isprintable())
# print("乐\n".isprintable())

# # 判断字符串所有字符是否都是十进制数字
# # 判断字符串中的所有字符是否都是数字字符（数学字符包含很广）
# # 与isdigit()类似，但更宽泛。它包括更多类型的数字字符
x = "114514"
print(x)
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x = "2²"
print(x)
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x = "ⅤⅢ"
print(x)
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())
x = "壹拾壹万肆仟伍佰壹拾肆"
print(x)
print(x.isdecimal())
print(x.isdigit())
print(x.isnumeric())

# # 判断字符串是否为Python中的合法标识符
# print("123ABC".isidentifier())
# print("_114514".isidentifier())
# # 判断字符串是否为Python中的关键字
# import keyword
# print(keyword.iskeyword("if"))
# print(keyword.iskeyword("abc"))
