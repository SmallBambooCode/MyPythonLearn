import numpy as np

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[9, 10], [7, 8]])

# 四则运算
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
# 矩阵点乘
a1 = np.array([[1, 0], [2, 4]])
a2 = np.array([[7, 1], [4, 0]])
print(np.dot(a1, a2))
# 普通乘法
print(a1 * a2)

# 三角函数
a1 = np.array([[0.2, 0.4], [0.5, 0.9]])
print(np.sin(a1))
print(np.cos(a1))
print(np.tan(a1))
print(np.arcsin(a1))
print(np.arccos(a1))
print(np.arctan(a1))

# 对整个数组求和
print(np.sum(a1))
# 沿着行的方向求和
print(np.sum(a1, axis=0))
# 沿着列的方向求和
print(np.sum(a1, axis=1))
# 对最后一个维度求和
print(np.sum(a1, axis=-1))


# import numpy as np
#
# a1 = np.array([[1, 2], [3, 4]])
# a2 = np.array([[9, 10], [7, 8]])
#
# # 数组统计
# # 返回数组中的最小值
# print(a1.min())
# # 返回数组中的最大值
# print(a1.max())
# # 返回数组中最小值的索引位置
# print(a1.argmin())
# # 返回数组中最大值的索引位置
# print(a1.argmax())
# # 返回数组所有元素的总和
# print(a1.sum())
# # 返回数组元素的累积和
# print(a1.cumsum())
# # 返回数组相邻元素的差值
# print(np.diff(a1))
# # 返回数组元素的平均值
# print(a1.mean())
# # 返回数组元素的中位数
# print(np.median(a1))
# # 返回数组元素的方差
# print(a1.var())
# # 返回数组元素的标准差
# print(a1.std())