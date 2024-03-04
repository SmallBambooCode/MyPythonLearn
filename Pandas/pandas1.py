import pandas as pd
import numpy as np

# # 创建序列
# s = pd.Series([1, 0, 0, 8, 6, 1, 1])
# # print(s)

# 准备数据
dates = pd.date_range('20240301', periods=6)
datas = np.random.randn(6, 4)
slot = ["早晨", "上午", "下午", "晚上"]
dict_data = {"姓名": ["Jerry", "Danny", "Jenny"], "年龄": np.arange(17, 20), "性别": "男"}
# 创建数据框(第一个单数是数据；第二个参数是行索引，用于标识DataFrame中的每一行；第三个参数是列索引，用于标识DataFrame中的每一列)
df = pd.DataFrame(datas, index=dates, columns=slot)
# print(df)
df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
# print(df2)
df3 = pd.DataFrame(dict_data)
# print(df3)

# # 查看数据框中数据的类型
# print(df.dtypes)
# print(df3.dtypes)
# # 输出行索引
# print(df3.index)
# # 输出列索引
# print(df3.columns)
# # 输出数据（DataFrame的第一个参数）
# print(df2.values)
# # 输出统计摘要（平均值、标准差、最小值、25%、50%、75% 四分位数和最大值等）
# print(df.describe())

# # 数据框的转置
# print(df)
# print(df.T)
# # print(df.transpose())

# 排序（ascending=False表示降序）
# 排序行索引（行标签），以降序排列
# 这里2>1>0
print(df3.sort_index(axis=0, ascending=False))
# 排序列索引（列标签），以降序排列
# 这里性别>年龄>姓名，检验：
print("性别" > "年龄" > "姓名")
print(df3.sort_index(axis=1, ascending=False))
# 按照“年龄”列的值排序，以降序排列
# 这里19>18>17
print(df3.sort_values(by="年龄", ascending=False))
