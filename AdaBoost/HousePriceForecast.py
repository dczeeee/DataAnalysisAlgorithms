from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import load_boston
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

boston = load_boston()
features = boston.data
labels = boston.target

train_x, test_x, train_y, test_y = train_test_split(features, labels, test_size=0.3, random_state=33)

# adaboost
adaboost = AdaBoostRegressor()
adaboost.fit(train_x, train_y)
pred_y = adaboost.predict(test_x)
mse = mean_squared_error(test_y, pred_y)
print("房价预测结果 ", pred_y)
print("均方误差 = ", round(mse, 2))

# dt
dt = DecisionTreeRegressor()
dt.fit(train_x, train_y)
pred_y = dt.predict(test_x)
mse = mean_squared_error(test_y, pred_y)
print("房价预测结果 ", pred_y)
print("均方误差 = ", round(mse, 2))

# knn
knn = KNeighborsRegressor()
knn.fit(train_x, train_y)
pred_y = knn.predict(test_x)
mse = mean_squared_error(test_y, pred_y)
print("房价预测结果 ", pred_y)
print("均方误差 = ", round(mse, 2))

