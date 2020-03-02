import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

pd.set_option('display.max_columns', None)

data = pd.read_csv('data.csv')

# 数据清洗
data.drop('id', axis=1, inplace=True)
data['diagnosis'].replace({'M': 1, 'B': 0}, inplace=True)

# 数据可视化
# 将肿瘤诊断结果可视化
sns.countplot(data['diagnosis'], label='Count')
plt.show()

# 特征选择
without_diagnosis = data.columns.values.tolist()
without_diagnosis.remove('diagnosis')

# 准备数据
train, test = train_test_split(data, test_size=0.3)
train_X = train[without_diagnosis]
train_y = train['diagnosis']
test_X = train[without_diagnosis]
test_y = train['diagnosis']

# 数据标准化
stand_scaler = StandardScaler()
train_X = stand_scaler.fit_transform(train_X)
test_X = stand_scaler.transform(test_X)

# 创建SVM分类器
model = svm.LinearSVC()
model.fit(train_X, train_y)
predict_y = model.predict(test_X)

print('准确率为：%.4lf' % accuracy_score(test_y, predict_y))
