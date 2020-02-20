# -*- coding:utf-8 -*-

from sklearn import preprocessing
import numpy as np

x = np.array([[0., -3., 1.],
              [3., 1., 2.],
              [0., 1., -1.]])

# min-max规范化, 按列进行计算的
min_max_scaler = preprocessing.MinMaxScaler()
min_max_x = min_max_scaler.fit_transform(x)
print(min_max_x)

# Z-Score规范化
# Z-Score 规范化可以直接将数据转化为正态分布的情况
scaled_x = preprocessing.scale(x)
print(scaled_x)

# 小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))   # ceil向上取整，floor向下取整
scaled_x_j = x/(10**j)
print(scaled_x_j)

