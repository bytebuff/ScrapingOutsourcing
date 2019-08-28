#! usr/bin/python
# -*- coding: utf-8 -*-
'''
@user: sean
@project_name:project
@file_name:demo 
@date:2019/5/6
'''

import codecs
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

names = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
# data = pd.read_csv('运维1.csv', names=names)
# print(data['feature1'])

# with open('test.txt', 'w', encoding='utf-8') as f:
#     for i in data['feature1']:
#         f.write(i + '\n')

#########################################################################
#                           第一步 计算TFIDF
corpus = []  # 文档预料 空格连接

# 读取预料 一行预料为一个文档
for line in open('cut_stop_word.txt', 'r', encoding='utf-8').readlines():
    corpus.append(line.strip())

# print(corpus)

#将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()

#该类会统计每个词语的tf-idf权值
transformer = TfidfTransformer()

#第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))

#获取词袋模型中的所有词语
word = vectorizer.get_feature_names()

#将tf-idf矩阵抽取出来，元素w[i][j]表示j词在i类文本中的tf-idf权重
weight = tfidf.toarray()
#
# #打印特征向量文本内容
# # print('Features length: ' + str(len(word)))
# # resName = "fidf_Result.txt"
# # result = codecs.open(resName, 'w', 'utf-8')
# # for j in range(len(word)):
# #     result.write(word[j] + ' ')
# # result.write('\r\n\r\n')
# #
# # # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
# # for i in range(len(weight)):
# #     print(u"-------这里输出第", i, u"类文本的词语tf-idf权重------")
# #     for j in range(len(word)):
# #         # print weight[i][j],
# #         result.write(str(weight[i][j]) + ' ')
# #     result.write('\r\n\r\n')
# # result.close()
#
# ########################################################################
# #                               第二步 聚类Kmeans
print('Start Kmeans:')
from sklearn.cluster import KMeans
clf = KMeans(n_clusters=10, random_state=10)
s = clf.fit(weight)
# print(s)

# 10个中心点
# print(clf.cluster_centers_)

# 每个样本所属的簇
print(clf.labels_)
i = 1

with open('cut_result.txt', 'w', encoding='utf-8') as f:
    while i <= len(clf.labels_):
        print(i, clf.labels_[i - 1])
        f.write(str(clf.labels_[i - 1]) + '\n')
        i = i + 1

# 用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print(clf.inertia_)