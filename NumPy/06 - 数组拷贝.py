import numpy as np

a = np.arange(12).reshape(3, 4)

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