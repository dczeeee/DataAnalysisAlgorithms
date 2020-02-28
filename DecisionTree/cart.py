# -*- coning:utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, export_graphviz
from sklearn.datasets import load_iris, load_boston, load_digits
import graphviz

# cart
# 分类树：预测有限分类
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

# scikit-learn CART创建分类树
# 准备数据集
iris = load_iris()
# 获取特征集和分类标识
features = iris.data
labels = iris.target
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


# 回归树：预测一个数值，连续的
# 用样本的离散程度来评价不纯度，与平均值的差值/方差
# 最小绝对偏差LAD/最小二乘偏差LSD（常用）
# CPP剪枝

# scikit-learn CART创建回归树
# 准备数据集
boston = load_boston()
# 探索数据
print(boston.feature_names)
# 获取特征集和房价
features = boston.data
prices = boston.target
# 随机抽取33%的数据作为测试集，其余训练集
train_features, test_features, train_prices, test_prices = train_test_split(features, prices, test_size=0.33)
# 创建CART回归树
dtr = DecisionTreeRegressor()
# 拟合构造CART回归树
dtr = dtr.fit(train_features, train_prices)
# 预测
predict_price = dtr.predict(test_features)
# 测试集的结果评价
print('回归树二乘偏差均值:', mean_squared_error(test_prices, predict_price))
print('回归树绝对值偏差均值:', mean_absolute_error(test_prices, predict_price))

'''
# 回归树可视化
# 参数是回归树模型名称，不输出文件
dot_data = export_graphviz(dtr, out_file=None)
graph = graphviz.Source(dot_data)
# render 方法会在同级目录下生成 Boston PDF文件，内容就是回归树。
graph.render('Boston')
'''

digits = load_digits()
features = digits.data
labels = digits.target
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
clf = DecisionTreeClassifier()
clf = clf.fit(train_features, train_labels)
test_predict = clf.predict(test_features)
print(accuracy_score(test_labels, test_predict))



