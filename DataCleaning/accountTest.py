import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_excel('./accountMessage.xlsx', header=0,
                   names=['index', 'no', 'name', 'age', 'weight', 'male1', 'male2', 'male3', 'female1', 'female2',
                            'female3'])
print(df)

# age最大频率
age_maxf = df['age'].value_counts().index[0]
# age平均
age_mean = int(df['age'].mean())
# 缺失值处理
df['age'].fillna(age_mean, inplace=True)

# 删除空行
df.dropna(subset=['name'], inplace=True)

# 列单位不统一
row_with_lbs = df['weight'].str.contains('lbs').fillna(False)
for i, lbs_row in df[row_with_lbs].iterrows():
    weight = int(float(lbs_row['weight'][:-3])/2.2)
    df.at[i, 'weight'] = '{}kgs'.format(weight)

# 合理性
# 删除非 ASCII 字符
df['name'].replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)

# 唯一性
# 将name拆分为first name和last name
df[['first_name', 'last_name']] = df['name'].str.split(expand=True)
df.drop('name', axis=1, inplace=True)

# 重复行
df.drop_duplicates(['first_name', 'last_name'], inplace=True)
print(df)

