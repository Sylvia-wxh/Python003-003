import pandas as pd
import numpy as np
import os


pwd = os.path.dirname(os.path.realpath(__file__))
data = os.path.join(pwd,'Contribution.xlsx')
excel = pd.read_excel(data)
# print(excel)

df = pd.DataFrame(excel)
# print(df)

columns = df.columns.values.tolist()
col_weight = []
col_return = []
for i in columns:
    if "Weight" in i:
        col_weight.append(i)
    elif "Return" in i:
        col_return.append(i)

df_weight = df[col_weight]
# print(df_weight)
df_return = df[col_return]
# print(df_return)

single = pd.DataFrame(df_weight.values * df_return.values/100, columns=[1, 2, 3, 4, 5, 6])
# # print(single)
single.to_excel('Contribution.xlsx', sheet_name='single')