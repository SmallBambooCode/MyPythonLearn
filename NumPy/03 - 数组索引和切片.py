import numpy as np

# 访问数组
a1 = np.array([[1, 2, 3], [4, 5, 6]])

# 获取第0行第1列的元素
print(a1[0, 1])

# 按条件筛选出指定元素
print(a1[a1 <= 4])
print(a1[(a1 <= 2) | (a1 >= 5)])
print(a1[(a1 % 2 == 0)])

# 获取第2行，第1~2列的元素
print(a1[1, 0:2])

# 每2个取1个
print(a1[1, ::2])

# 逆序输出
print(a1[1, ::-1])