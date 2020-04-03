import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
import warnings
from itertools import product
from datetime import datetime

warnings.filterwarnings('ignore')

df = pd.read_csv('./shanghai_1990-12-19_to_2019-2-28.csv')
df.Timestamp = pd.to_datetime(df.Timestamp)
df.index = df.Timestamp

# 数据探索
print(df.head())


# 设置参数范围
ps = range(0, 3)
qs = range(0, 3)
parameters = product(ps, qs)
parameters_list = list(parameters)

# 每天
# 寻找最优ARMA模型参数，即best_aic最小
results = []
best_aic = float("inf")  # 正无穷
for param in parameters_list:
    try:
        model = ARMA(df.Price, order=(param[0], param[1])).fit()
    except ValueError:
        print('参数错误:', param)
        continue
    aic = model.aic
    if aic < best_aic:
        best_model = model
        best_aic = aic
        best_param = param
    results.append([param, model.aic])

# 输出最优模型
result_table = pd.DataFrame(results)
result_table.columns = ['parameters', 'aic']
print('最优模型:', best_model.summary())
# 上证指数预测
df2 = df[['Price']]
date_list = pd.date_range('2019-03-01', '2020-04-02', periods=None, freq='D')
future = pd.DataFrame(index=date_list, columns=df2.columns)
df2 = pd.concat([df2, future])

df2['forecast'] = best_model.predict(start=0, end=7291)

plt.figure(figsize=(20, 7))
df2.Price.plot(label='实际金额')
df2.forecast.plot(color='r', ls='--', label='预测金额')
plt.legend()
plt.title('上证指数（日）')
plt.xlabel('时间')
plt.ylabel('RMB')
plt.show()

print(df2)


