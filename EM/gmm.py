from sklearn.mixture import GaussianMixture
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data_ori = pd.read_csv('heros.csv', encoding='gbk')

print(data_ori.columns)
print(data_ori.info())
print(data_ori.describe())

# 设置plt正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
sns.countplot(data_ori['主要定位'])
plt.show()

features = [u'最大生命',u'生命成长',u'初始生命',u'最大法力', u'法力成长',u'初始法力',u'最高物攻',u'物攻成长',u'初始物攻',u'最大物防',u'物防成长',u'初始物防', u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data_ori[features]

# 用热力图呈现features_mean字段之间的相关性
corr = data[features].corr()
plt.figure(figsize=(14,14))
# annot=True  显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()

# 相关性大的属性保留一个，因此可以对属性进行降维
features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血', u'最大每5秒回蓝', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data_ori[features_remain]

# 数据清洗
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%'))/100)
data[u'攻击范围'] = data[u'攻击范围'].map({'远程': 1, '近战': 0})

# 标准化
ss = StandardScaler()
data = ss.fit_transform(data)

# 构造gmm聚类
gmm = GaussianMixture(n_components=30, covariance_type='full')
gmm.fit(data)

# 训练数据
prediction = gmm.predict(data)
print(prediction)

# 将分组结果输出到CSV文件中
data_ori.insert(0, '分组', prediction)
data_ori.to_csv('./hero_out.csv', index=False, sep=',')



