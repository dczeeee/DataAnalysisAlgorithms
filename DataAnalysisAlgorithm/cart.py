# -*- coning:utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# cart
# 回归树：预测一个数值；分类树：预测有限分类
# 基尼系数，越小纯度越高
# GINI(t) = 1 - ∑[p(Ck|t)]^2
# 集合 1：6 个都去打篮球
# 集合 2：3 个去打篮球，3 个不去打篮球
G1 = 1 - (6/6)**2
G2 = 1 - ((3/6)**2 + (3/6)**2)
print(G1, G2)
# 父节点的基尼系数等于子节点基尼系数归一化之和
G = 6/12 * G1 + 6/12 * G2
print(G)

# scikit-learn
# 准备数据集
iris = load_iris()
# 获取特征集和分类标识
features = iris.data
print(features)
labels = iris.target
print(labels)
# 随机抽取33%的数据作为测试集，其余为训练集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
# 创建CART分类树
clf = DecisionTreeClassifier(criterion='gini')
# 拟合构造CART分类树
clf = clf.fit(train_features, train_labels)
# 用CART分类树做预测
test_predict = clf.predict(test_features)
# 预测结果与测试集结果作比对
score = accuracy_score(test_labels, test_predict)
print("CART分类树准确率 %.4lf" % score)




