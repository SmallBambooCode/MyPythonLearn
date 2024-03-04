# import numpy as np
#
# a1 = np.array([[0.5, 0.7], [0.1, 0.2]])
# # 数组维度
# print(a1.ndim)
# # 数组形状（尺寸）
# print(a1.shape)
# # 数组大小（元素数量）
# print(a1.size)

import numpy as np

a1 = np.array([[0.5, 0.7], [0.1, 0.2]])

# 现有数组转换类型，返回新数组
a2 = a1.astype(np.float)
print(a2)

# 返回介于某个区间的等距分布的值
a4 = np.linspace(0, 10, 5)
print(a4)

# 重新设置维度
a3 = a2.reshape(4, 1)
print(a3)

# 排序(逐行)
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a1.sort()
print(a1)

# 转置
print(a1)
print(a1.transpose())
# print(a1.T)

# 指定最小和最大数(例如小于0的变为0,大于4的变为4,在卷积操作用的比较多,把超过255的变为255)
print(a1.clip(0, 4))

# 将多维数组压扁,返回迭代器
for i in a1.flat:
    print(i)