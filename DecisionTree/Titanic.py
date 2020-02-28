import pandas as pd

# 数据加载
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

'''
# 数据探索
print(train_data.info())
print('-'*30)
print(train_data.describe())
print('-'*30)
print(train_data.describe(include='O'))  # 查看字符串类型（非数字）的整体情况
print('-'*30)
print(train_data.head())
print('-'*30)
print(train_data.tail())

print(test_data.info())
print('-'*30)
print(test_data.describe())
print('-'*30)
print(test_data.describe(include='O'))  # 查看字符串类型（非数字）的整体情况
print('-'*30)
print(test_data.head())
print('-'*30)
print(test_data.tail())
'''
# Age、Fare、Cabin、Embarked存在缺失，Age、Fare可用平均值补全，Cabin缺失太多，Embarked用众数值补全

# 数据清洗
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(), inplace=True)

train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(), inplace=True)

# print(train_data['Embarked'].value_counts())
# S    644
# C    168
# Q     77
# S最多

train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择

# 特征选择
# 乘客编号，姓名，票号对分类没有影响，Cabin缺失值太多，放弃，剩余特征加入
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]








