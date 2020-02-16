import requests

'''
# Get 把参数包含在 url 中，而 Post 通过 request body 来传递参数
r = requests.get('http://www.douban.com')
r = requests.post('http://xxx.com', data = {'key':'value'})
'''

import json

jsonData = '{"a": 1, "b": 2, "c": 3, "d": 4}'   # 测试发现必须单引号括双引号，不然报错
input = json.loads(jsonData)
print(input)
