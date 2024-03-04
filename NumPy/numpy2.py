import numpy as np
a1 = np.array([[0.5, 0.7], [0.1, 0.2]])
print(a1)
# 数组维度
print(a1.ndim)
# 数组形状（尺寸）
print(a1.shape)
# 数组大小（元素数量）
print(a1.size)
# 现有数组转换类型，返回新数组
a2 = a1.astype(np.float)
print(a2)
# 重新设置维度
a3 = a2.reshape(4, 1)
print(a3)

# 三角函数
print(np.sin(a1))
print(np.cos(a1))
print(np.tan(a1))
print(np.arcsin(a1))
print(np.arccos(a1))
print(np.arctan(a1))

a1 = np.array([[1, 0],
               [2, 4]])
a2 = np.array([[7, 1],
               [4, 0]])
# 矩阵点乘
print(np.dot(a1, a2))
# 普通乘法
print(a1 * a2)

a1 = np.array([[1, 0, 9, 6],
               [2, 4, 3, 7],
               [5, 8, -1, -2]])

# 排序(逐行)
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

a1 = np.array([[1, 2, 3],
               [5, 6, 7]])
a2 = np.array([[7, 8, 9],
               [9, 8, 7]])

# 上下合并
print(np.vstack((a1, a2)))
# 左右合并
print(np.hstack((a1, a2)))
# 指定维度合并
print(np.concatenate((a1,a2), axis=0))
print(np.concatenate((a1,a2), axis=1))

a1 = np.arange(12).reshape(3, 4)
print(a1)
# 等块分割(参数为数组对象，分成几块，按照什么维度去分)
print(np.split(a1, 2, axis=1))
print(np.split(a1, 3, axis=0))
# 不等块分割(参数为数组对象，分成几块，按照什么维度去分)
print(np.array_split(a1, 2, axis=0))

a = np.arange(12).reshape(3,4)
# 浅拷贝
b = a
# 深拷贝
c = a.copy()
print(a)
a[0, 0] = 12
print(a)
print(b)
print("a,b的id分别是：", end="")
print(id(a), id(b))
print(c)
print("a,c的id分别是：", end="")
print(id(a), id(c))
