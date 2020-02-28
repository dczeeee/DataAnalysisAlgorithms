import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import cross_val_score
import graphviz

# 数据加载
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
# Titanic_Data
# 数据集中的字段描述：
# PassengerId	乘客编号
# Survived	是否幸存
# Pclass	船票等级
# Name	乘客姓名
# Sex	乘客性别
# SibSp	亲戚数量（兄妹、配偶数）
# Parch	亲戚数量（父母、子女数）
# Ticket	船票号码
# Fare	船票价格
# Cabin	船舱
# Embarked	登录港口

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

# 特征值不都是数值类型，可以使用 DictVectorizer 类进行转化
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))

# print(dvec.feature_names_)
# ['Age', 'Embarked=C', 'Embarked=Q', 'Embarked=S', 'Fare', 'Parch', 'Pclass', 'Sex=female', 'Sex=male', 'SibSp']

# 决策树模型
# 构造ID3决策树
clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features, train_labels)

# 模型预测，评估
test_features = dvec.transform(test_features.to_dict(orient='record'))
predict_labels = clf.predict(test_features)

# 得到决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score准确率为 %.4lf' % acc_decision_tree)

# 由于不知道测试集的真实结果，用训练集score会很接近100%
# 故选用交叉验证

# 交叉验证
print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

# 决策树可视化
dot_data = export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.view('Titanic')


