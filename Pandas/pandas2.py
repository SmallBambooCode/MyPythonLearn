import pandas as pd
import numpy as np
dates = pd.date_range('20240301', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=["A", "B", "C", "D"])
print(df)

print(df["A"])
# print(df.A)

# 左闭右开
print(df[0:3])
# 闭区间
print(df["20240301":"20240303"])

# location(loc)通过标签来选择数据
print(df.loc["20240301":"20240303"])
# 搜索列中的A和B，全部输出行
print(df.loc[:,["A","B"]])
# 搜索列中的A和B，行中的20240301
print(df.loc["20240301",["A","B"]])

# integer location(iloc)通过整数位置来选择数据
# 输出第3行
print(df.iloc[3])
# 输出第3行，第0列
print(df.iloc[3, 0])
# print(df.iloc[3][0])
# 输出第3~5行，第0~3列
print(df.iloc[3:6, 0:4])
# 输出第1,3,5,行，第0~3列
print(df.iloc[::2, 0:4])
# 输出指定行，第0~3列
print(df.iloc[[1,2,5], 0:4])

# iloc和loc混合使用
print(df.ix[:3, ["A", "C"]])
print(df.ix[2:6, ["A"]])

# 真假筛选
# 输出A列中大于8的数据
print(df[df.A > 8])
