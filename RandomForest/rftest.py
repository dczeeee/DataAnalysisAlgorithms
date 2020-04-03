# -*- coding: utf-8 -*-
# 使用RandomForest对IRIS数据集进行分类
# 利用GridSearchCV寻找最优参数
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
parameters = {"n_estimators": range(1, 11)}

iris = load_iris()

clf = GridSearchCV(estimator=rf, param_grid=parameters)

clf.fit(iris.data, iris.target)

print("最优分数： %.4lf" % clf.best_score_)
print("最优参数：", clf.best_params_)
