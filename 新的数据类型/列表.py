# # 创建一个列表
# rhyme = [1, 2, 3, 4, 5, "上山打老虎"]
# for i in rhyme:
#     print(i, end=" ")
# print()
# # 单独访问某一个元素
# print(rhyme[0])
# # -1是倒着数
# print(rhyme[-1])
# # 切片 左闭右开！
# print(rhyme[0:3])
# print(rhyme[3:6])
# print(rhyme[:3])
# print(rhyme[3:])
# print(rhyme[:])
# print(rhyme[0:6:2])
# print(rhyme[::2])
# # 倒序输出
# print(rhyme[::-1])

codingLang = ['javascript', 'python', 'java', 'c++', 'javascript']
print(codingLang)
# # 增
# codingLang.append('c')
# # codingLang[len(codingLang):] = ['c']
# print(codingLang)
# codingLang.extend(['ruby', 'php', 'go'])
# # codingLang[len(codingLang):] = ['ruby', 'php', 'go']
# print(codingLang)
# # 插入
# codingLang.insert(1, 'css')
# print(codingLang)
# codingLang.insert(len(codingLang), 'c#')
# print(codingLang)


# # 删
# # 根据元素值删除
# codingLang.remove('javascript')
# print(codingLang)
# # 根据位置删除
# codingLang.pop(1)
# print(codingLang)
# # 清空列表
# codingLang.clear()
# print(codingLang)


# # 改
# codingLang[0] = 'typescript'
# print(codingLang)
# # 使用切片连续替换
# codingLang[1:] = ['php', 'ruby', 'c#']
# print(codingLang)
# # 排序（从小到大）
# codingLang.sort()
# print(codingLang)
# # 排序（从大到小）
# codingLang.reverse()
# # codingLang.sort(reverse=True)
# print(codingLang)

# # 查
# # 查找元素有几个
# print(codingLang.count('javascript'))
# # 查找元素的索引
# print(codingLang.index('java'))
# codingLang[codingLang.index('java')] = 'c'
# print(codingLang)
# # 浅拷贝
# cl1 = codingLang
# cl2 = codingLang.copy()
# # cl2 = codingLang[:]
# print(cl2)

# 创建一个列表
rhyme = [1, 2, 3, 4, 5, "上山打老虎"]
for i in rhyme:
    print(i, end=" ")
print()
# 单独访问某一个元素
print(rhyme[0])
# -1是倒着数
print(rhyme[-1])
