import jieba
import numpy as np

str_a = "这只皮靴号码大了，那只号码合适"
str_b = "这只皮靴号码不小，那只更合适"

list_a = [i for i in jieba.cut(str_a, cut_all=False) if i != '，']
list_b = [i for i in jieba.cut(str_b, cut_all=False) if i != '，']
print(list_a)
print(list_b)

set_ab = set(list_a).union(set(list_b))
print(set_ab)

i = 0
word_dict = dict()
for word in set_ab:
    word_dict[word] = i
    i += 1
print(word_dict)

cnt_a = [0] * len(word_dict)
for word in list_a:
    cnt_a[word_dict[word]] += 1
cnt_b = [0] * len(word_dict)
for word in list_b:
    cnt_b[word_dict[word]] += 1
print(cnt_a)
print(cnt_b)

len_a = np.sqrt(sum(i ** 2 for i in cnt_a))
len_b = np.sqrt(sum(i ** 2 for i in cnt_b))

cos_ab = np.dot(cnt_a, cnt_b) / (len_a * len_b)
print(cos_ab)
