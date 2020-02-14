# -*- coding:utf-8 -*-

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

'''
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))  # 在 n 次方中，x2 数组中的元素实际上是次方的次数，x1 数组的元素为基数。
print(np.remainder(x1, x2))
print(np.mod(x1, x2))
'''

'''
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)

print(np.amax(a))
print(np.amax(a, 0))    # axis=0 横轴
print(np.amax(a, 1))
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))

# 统计最大值与最小值之差 ptp()
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

# 统计数组的百分位数percentile(a,p) a是数组，p是所占百分位置，取值0-100
print(np.percentile(a, 5))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))


# 统计数组中的中位数 median()、平均数 mean()
print(np.median(a))
print(np.median(a, 0))
print(np.median(a, 1))
print(np.mean(a))
print(np.mean(a, 0))
print(np.mean(a, 1))
'''

'''
# 统计数组中的加权平均值 average()
a = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a))
print(np.average(a, weights=wts))
'''

'''
# 统计数组中的标准差 std()、方差 var()
a = np.array([1, 2, 3, 4])
print(np.std(a))
print(np.var(a))
'''

'''
# numpy排序
# sort(a, axis=-1, kind=‘quicksort’, order=None)，默认情况下使用的是快速排序；在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序
a = np.array([[4, 3, 2], [2, 4, 1]])
print(a)
print(np.sort(a, axis=None, kind='mergesort'))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
'''

'''
为什么要用 NumPy 数组结构而不是 Python 本身的列表 list？
1.因为list存储的元素是分散在内存中各个位置的，而numpy存储在一段连续的内存空间，这样计算遍历元素时，无需对地址进行查找，提高了效率
2.内存访问模式中，会直接把字节块从RAM拿到CPU寄存器，数据连续存储可以利用现代CPU的矢量化指令计算
3.numpy矩阵可以采用多线程的方式，充分领多核CPU计算资源，大大提高了计算效率
'''

persontype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['U32', 'i', 'i', 'i']
})

person = np.array([('张飞', 66, 65, 30), ('关羽', 95, 85, 98), ('赵云', 93, 92, 96), ('黄忠', 90, 88, 77), ('典韦', 80, 90, 90)],
                  dtype=persontype)
print(person)

name = person[:]['name']
chinese = person[:]['chinese']
english = person[:]['english']
math = person[:]['math']

for i in [chinese, english, math]:
    print(np.average(i))
    print(np.max(i))
    print(np.min(i))
    print(np.var(i))
    print(np.std(i))

print(sorted(person, key=lambda a: a[1]+a[2]+a[3], reverse=True))

