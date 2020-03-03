from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

digits = load_digits()
data = digits.data
print(digits.images[0])
print(digits.target[0])
plt.gray()
plt.imshow(digits.images[0])
plt.show()

# 划分数据集
train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.3, random_state=33)

# 标准化
ss = StandardScaler()
train_x = ss.fit_transform(train_x)
test_x = ss.transform(test_x)

# 创建KNN分类器
knn = KNeighborsClassifier()
knn.fit(train_x, train_y)
predict_y = knn.predict(test_x)

print('KNN准确率为：%.4lf' % accuracy_score(predict_y, test_y))


# 创建SVM分类器
svm = svm.SVC()
svm.fit(train_x, train_y)
predict_y = svm.predict(test_x)
print('SVM准确率: %0.4lf' % accuracy_score(test_y, predict_y))
# 采用Min-Max规范化
mm = MinMaxScaler()
train_mm_x = mm.fit_transform(train_x)
test_mm_x = mm.transform(test_x)
# 创建Naive Bayes分类器
# 多项式贝叶斯不能传入负值
mnb = MultinomialNB()
mnb.fit(train_mm_x, train_y)
predict_y = mnb.predict(test_mm_x)
print("多项式朴素贝叶斯准确率: %.4lf" % accuracy_score(test_y, predict_y))
# 创建CART决策树分类器
dtc = DecisionTreeClassifier()
dtc.fit(train_mm_x, train_y)
predict_y = dtc.predict(test_mm_x)
print("CART决策树准确率: %.4lf" % accuracy_score(test_y, predict_y))
