import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

# 加载数据
data = pd.read_csv('data.csv', encoding='gbk')

train_x = data[["2019年国际排名", "2018世界杯", "2015亚洲杯"]]

# 归一化
minmax_scaler = preprocessing.MinMaxScaler()    # StandardScaler均值0方差1标准化
train_x = minmax_scaler.fit_transform(train_x)

# KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)

# 结果合并
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类'}, axis=1, inplace=True)
print(result)


