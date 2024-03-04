import numpy as np

# 创建数组
a1 = np.array([1, 2, 3, 4, 5])
print(a1)

# 创建全零数组
a2 = np.zeros((3, 2))
print(a2)

# 创建全1数组
a3 = np.ones((3, 2))
print(a3)

# 创建递增或递减数列
a4 = np.arange(3, 7)
a5 = np.arange(7, 3, -1)
print(a4)
print(a5)

# 生成随机数组
a7 = np.random.rand(4, 3)
print(a7)

# 数组默认数据类型为64位浮点数
print(a3.dtype)

# 创建数组时指定其他数据类型
a8 = np.ones((4, 3), dtype=np.int32)
print(a8)

# 现有数组转换类型，返回新数组
a9 = a8.astype(np.float)
print(a9)