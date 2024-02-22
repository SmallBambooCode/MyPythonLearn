import random
x = random.getstate()
for i in range(3):
    print(random.randint(1, 10))

# 设置生成器随机状态
random.setstate(x)
# “随机数”重现了！
print("“随机数”重现了！")
for i in range(3):
    print(random.randint(1, 10))