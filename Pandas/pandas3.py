import pandas as pd
import numpy as np
dates = pd.date_range('20240301', periods=6)
df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=["A", "B", "C", "D"])

# # 修改指定单个数据
# df.iloc[2, 2] = 10010
# df.loc["20240303", "D"] = 10086
# print(df)
#
# # 条件修改
# # 列A中大于10的值改为10
# df.A[df.A > 10] = 10
# # 列A中大于5的，在列B的值改为0
# df.B[df.A > 5] = 0
# print(df)
# # 新建F列，默认值设置为0
# df["F"] = 0
# # 使用序列Series新建一列
# df["E"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20240301', periods=6))
# print(df)

# 处理丢失数据
df.iloc[[0, 1], [1, 2]] = np.nan
print(df)

# 丢弃NaN数据，axis为丢掉的维度
# 丢掉行
print(df.dropna(axis=0, how="any"))  # how={"any", "how"} any是只要有NaN就丢掉，all是在指定的维度全部为NaN时才丢掉
# 丢掉列
print(df.dropna(axis=1, how="any"))

# 填充NaN数据
print(df.fillna(value=0))

# 检查有没有NaN，数据替换为True or False
print(df.isnull())
# 至少有一个True则输出True
print(np.any(df.isnull()) == True)
