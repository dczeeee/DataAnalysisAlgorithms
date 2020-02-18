import pandas as pd

df = pd.read_excel('./foodInformation.xlsx')
print(df)

# 空值删除
df.dropna(inplace=True)

# 负值变正
df['ounces'] = df['ounces'].apply(lambda x: abs(x))

# 全部小写
df['food'] = df['food'].str.lower()

df.groupby(['food', 'animal']['ounces'].mean())



print(df)