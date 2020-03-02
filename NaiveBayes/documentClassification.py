# -*- coding:utf-8 -*-
import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')


def cut_words(file_path):
    text_with_spaces = ''
    text = open(file_path, 'r', encoding='gb18030').read()
    textcut = jieba.cut(text)
    for word in textcut:
        text_with_spaces += word + ' '
    return text_with_spaces


def load_file(file_dir, label):
    file_list = os.listdir(file_dir)
    words_list = []
    label_list = []
    for file in file_list:
        file_path = file_dir + '/' + file
        words_list.append(cut_words(file_path))
        label_list.append(label)
    return words_list, label_list


# 训练数据
train_words_list_1, train_label_list_1 = load_file('text classification/train/体育', '体育')
train_words_list_2, train_label_list_2 = load_file('text classification/train/女性', '女性')
train_words_list_3, train_label_list_3 = load_file('text classification/train/文学', '文学')
train_words_list_4, train_label_list_4 = load_file('text classification/train/校园', '校园')

train_words_list = train_words_list_1 + train_words_list_2 + train_words_list_3 + train_words_list_4
train_label_list = train_label_list_1 + train_label_list_2 + train_label_list_3 + train_label_list_4

# 测试数据
test_words_list_1, test_label_list_1 = load_file('text classification/test/体育', '体育')
test_words_list_2, test_label_list_2 = load_file('text classification/test/女性', '女性')
test_words_list_3, test_label_list_3 = load_file('text classification/test/文学', '文学')
test_words_list_4, test_label_list_4 = load_file('text classification/test/校园', '校园')

test_words_list = test_words_list_1 + test_words_list_2 + test_words_list_3 + test_words_list_4
test_label_list = test_label_list_1 + test_label_list_2 + test_label_list_3 + test_label_list_4

# 停用词
stop_words = open('text classification/stop/stopword.txt', 'r', encoding='utf-8-sig').read()
# stop_words = stop_words.encode('utf-8').decode('utf-8-sig')  # 列表头部\ufeff处理
stop_words = stop_words.split('\n')

# 计算单词权重
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)

train_features = tf.fit_transform(train_words_list)
test_features = tf.transform(test_words_list)

# 多项式贝叶斯分类器
clf = MultinomialNB(alpha=0.001)
clf.fit(train_features, train_label_list)
predict_label = clf.predict(test_features)

# 计算准确率
print('准确率为: %.4lf' % accuracy_score(test_label_list, predict_label))


