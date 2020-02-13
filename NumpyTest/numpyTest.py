import numpy as np
'''
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1][1] = 10
print(a.shape)
print(b.shape)
print(b.dtype)
print(b)
'''

'''
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']
})
peoples = np.array([('wanghy', 22, 0, 0, 0), ('liliming', 21, 100, 100, 100)], dtype=persontype)

print(peoples)

ages = peoples[:]['age']
print(ages)
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(np.mean(ages))
print(np.mean(chineses))
print(np.mean(maths))
print(np.mean(englishs))
'''

x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)

