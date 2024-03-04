import pandas as pd
import numpy as np

# df1 = pd.DataFrame(np.ones((3,4))*0, columns=list('ABCD'))
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=list('ABCD'))
# df3 = pd.DataFrame(np.ones((3,4))*2, columns=list('ABCD'))
# print(df1)
# print(df2)
# print(df3)

# # 合并数据框（concatenating）axis指定合并维度，ignore_index为忽略行索引
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# print(res)

# join, ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3,4))*0, columns=list("ABCD"), index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=list("BCDE"), index=[2,3,4])
res = pd.concat([df1, df2], axis=1, join='outer')
res2 = pd.concat([df1, df2], axis=1, join='inner')

print(res)
print(res2)