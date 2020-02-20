import pandas as pd

df = pd.read_excel('./foodInformation.xlsx')
# print(df)

# 空值删除
df.dropna(inplace=True)

# 负值变正
df['ounces'] = df['ounces'].apply(lambda x: abs(x))

# 全部小写
df['food'] = df['food'].str.lower()

# 查找food重复记录，分组求其平均
d_rows = df[df['food'].duplicated(keep=False)]
print(d_rows)
g_items = d_rows.groupby('food').mean()
print(g_items)
g_items['food'] = g_items.index
print(g_items)

# 遍历将重复food的值赋给df
for i, row in g_items.iterrows():
    df.loc[df.food == row.food, 'ounces'] = row.ounces
df.drop_duplicates(inplace=True)

# 重设索引值
df.index = range(len(df))
print(df)
