import numpy as np
# 创建一个数组
a1 = np.array([1, 2, 3, 4, 5])
print(a1)
# 创建一个全零数组（传入数组尺寸，此处为3行2列）
a2 = np.zeros((3, 2))
print(a2)
# 使用shape方法查看数组尺寸
print(a2.shape)
# 创建一个全1数组（传入数组尺寸，此处为3行2列）
a3 = np.ones((3, 2))
print(a3)
# 创建递增或递减数列（左闭右开）
a4 = np.arange(3, 7)
a5 = np.arange(7, 3, -1)
print(a4)
print(a5)
# 返回介于某个区间，等距分布的值
a6 = np.linspace(0, 10, 5)
print(a6)
# 生成随机数组（4,3为4行3列）
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

a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[9, 10], [7, 8]])
# 四则运算
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)

a1 = np.array([8, 5, 4, 6, 7, 1, 9])
# 返回数组中的最值
print(a1.min())
print(a1.max())
# 返回数组中的最值的索引
print(a1.argmin())
print(a1.argmax())
# 求和
print(a1.sum())
# 累加
print(a1.cumsum())
# 累差
print(np.diff(a1))
# 求平均值，中位数
print(a1.mean())
print(np.median(a1))
# 求方差，标准方差
print(a1.var())
print(a1.std())


arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 对整个数组求和
print(np.sum(arr))

# 沿着行的方向求和
print(np.sum(arr, axis=0))

# 沿着列的方向求和
print(np.sum(arr, axis=1))

# 对最后一个维度求和
print(np.sum(arr, axis=-1))

a1 = np.array([[1, 2, 3],
               [4, 5, 6]])
# 访问数组
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
