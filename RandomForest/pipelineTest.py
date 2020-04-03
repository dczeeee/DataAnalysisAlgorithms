# -*- coding: utf-8 -*-
# 使用RandomForest对IRIS数据集进行分类
# 利用GridSearchCV寻找最优参数,使用Pipeline进行流水作业

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

rf = RandomForestClassifier()
parameters = {"randomforestclassifier__n_estimators": range(1, 11)}

iris = load_iris()

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('randomforestclassifier', rf)
])

clf = GridSearchCV(estimator=pipeline, param_grid=parameters)

# 对iris数据集进行分类
clf.fit(iris.data, iris.target)

print("最优分数： %.4lf" % clf.best_score_)
print("最优参数：", clf.best_params_)



