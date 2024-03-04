print(100000000000000000000/114514)
print(0.1+0.2)
print(int("1010", base=2), end="，")
print(int("1010", base=10))

# 使用decimal模块
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = decimal.Decimal('0.3')
print(a+b)
print(a+b == c)

# 复数
# 使用 complex() 函数创建复数对象
z1 = complex(2, 3)
print(z1)
# 直接定义一个复数
z2 = 4 + 5j
print(z2)
# 加法
print(z1 + z2)
# 减法
print(z1 - z2)
# 乘法
print(z1 * z2)
# 除法
print(z1 / z2)
# 求模
print(abs(z1))
# 求共轭
print(z1.conjugate())
# 求实部和虚部
print(z1.real, z1.imag)


# 布尔类型
print(bool("False"))
print(bool("0"))
print(bool(0))
print(bool([]))
print(bool((9, 5)))
print(bool(0j))
print(bool(0.00000))
