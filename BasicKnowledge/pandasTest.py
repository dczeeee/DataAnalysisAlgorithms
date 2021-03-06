import pandas as pd
from pandas import Series, DataFrame

'''
x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

d = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
x3 = Series(d)
print(x3)
'''

'''
data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)
'''

df = pd.read_excel('./data.xlsx', header=None, names=['English', 'Math', 'Chinese'])
# print(df)
# df.to_excel('data1.xlsx')

# 数据清洗
'''
# 删除行列
df = df.drop(index=0)
df = df.drop(columns=['English'])
print(df)

# 重命名列名
df.rename(columns={'Chinese': 'YuWen'}, inplace=True)
print(df)

# 去重复行
df = df.drop_duplicates()

print(df.dtypes)
# 更改数据格式
df['Math'] = df['Math'].astype('str')
print(df.dtypes)

# str删除头尾指定字符，默认空格，不能删除中间
s = 'ojbk1$'
print(s.strip('1$'))

# 大小写转化
#全部大写
df.columns = df.columns.str.upper()
#全部小写
df.columns = df.columns.str.lower()
#首字母大写
# df.columns = df.columns.str.title()
print(df)

# 查找空值
print(df.isnull())
# 查看哪列存在空值
print(df.isnull().any())
'''

'''
# 使用 apply 函数对数据进行清洗
def double_df(x):
    return x * 2


df['English'] = df['English'].apply(double_df)
print(df)

# 增加列
def plus(df, m, n):
    df['new1'] = (df['English']+df['Math'])*m
    df['new2'] = (df['English']+df['Math'])*n
    return df

df = df.apply(plus, axis=1, args=(2,3))
print(df)
'''

# print(df.describe())

'''
# 数据表合并
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
print(df1)
print(df2)

# a.基于指定列连接
df3 = pd.merge(df1, df2, on='name')
print(df3)
# b.inner内连接，inner是merge的默认情况，相当于交集
df4 = pd.merge(df1, df2, how='inner')
print(df4)
# c.left左连接，以第一个dataframe为主，第二个做补充
df5 = pd.merge(df1, df2, how='left')
print(df5)
# d.right右连接，与left相反
df6 = pd.merge(df1, df2, how='right')
print(df6)
# e.outer外连接
df7 = pd.merge(df1, df2, how='outer')
print(df7)
'''

data = {'chinese': [66, 95, 95, 90, 80, 80], 'english': [65, 85, 92, 88, 90, 90], 'math': [None, 98, 96, 77, 90, 90]}
scoreDf = DataFrame(data, index=['zf', 'gy', 'zy', 'hz', 'dw', 'dw'], columns=['chinese', 'english', 'math'])
print(scoreDf)
# 1.去重复行
scoreDf = scoreDf.drop_duplicates()
print(scoreDf)
# 2.补缺值，用数学平均成绩补zf数学
print(scoreDf.isnull())
scoreDf['math'].fillna(scoreDf['math'].mean(), inplace=True)
print(scoreDf)


# 3.增加总分列
def total(df):
    df['total'] = df['chinese'] + df['english'] + df['math']
    return df


scoreDf = scoreDf.apply(total, axis=1)
print(scoreDf)
