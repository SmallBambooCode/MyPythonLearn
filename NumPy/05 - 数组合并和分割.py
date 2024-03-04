import numpy as np

a1 = np.arange(6).reshape(2, 3)
a2 = np.array([[7, 8, 9], [9, 8, 7]])

# 上下合并
print(np.vstack((a1, a2)))

# 左右合并
print(np.hstack((a1, a2)))

# 指定维度合并
print(np.concatenate((a1, a2), axis=0))
print(np.concatenate((a1, a2), axis=1))

a3 = np.arange(12).reshape(3, 4)
# 等块分割
print(np.split(a3, 2, axis=1))
print(np.split(a3, 3, axis=0))

# 不等块分割
print(np.array_split(a3, 2, axis=0))
