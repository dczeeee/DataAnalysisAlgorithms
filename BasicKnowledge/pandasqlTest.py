import pandas as pd
from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births

df = DataFrame({'name': ['zf', 'gy', 'a', 'b', 'c'], 'data1': range(5)})
print(df)
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df where name='zf'"
print(pysqldf(sql))
