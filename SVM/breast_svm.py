import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', None)

data = pd.read_csv('data.csv')

# 数据探索
# print(data.columns)
# print(data.info())
# print('-'*30)
# print(data.describe())

# 数据清洗
features_mean = list(data.columns[2:12])
features_se = list(data.columns[12:22])
features_worst = list(data.columns[22:32])
data.drop('id', axis=1, inplace=True)
data['diagnosis'].replace({'M': 1, 'B': 0}, inplace=True)

# 数据可视化
# 将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'], label='Count')
plt.show()
# 用热力图呈现features_mean字段之间的相关性
corr = data[features_mean].corr()
plt.figure(figsize=(14, 14))
# annot=True显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()

# 特征选择
features_remain = ['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean', 'symmetry_mean', 'fractal_dimension_mean']

# 准备数据
train, test = train_test_split(data, test_size=0.3)
train_X = train[features_remain]
train_y = train['diagnosis']
test_X = test[features_remain]
test_y = test['diagnosis']

# 数据标准化
stand_scaler = StandardScaler()
train_X = stand_scaler.fit_transform(train_X)
test_X = stand_scaler.transform(test_X)

# 创建SVM分类器
model = svm.SVC()
model.fit(train_X, train_y)
predict_y = model.predict(test_X)

print('准确率为：%.4lf' % accuracy_score(test_y, predict_y))



