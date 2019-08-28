import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


# 切词
def jieba_tokenize(text):
    return list(jieba.cut(text) )

'''
tokenizer: 指定分词函数
lowercase: 在分词之前将所有的文本转换成小写，因为涉及到中文文本处理，
所以最好是False
'''
tfidf_vectorizer = TfidfVectorizer(tokenizer=jieba_tokenize, lowercase=False)

# 需要进行聚类的文本集
# text_list = ["今天天气真好啊啊啊啊", "小明上了清华大学", \
# "我今天拿到了Google的Offer", "清华大学在自然语言处理方面真厉害","天气不错啊"]
text_list = []
with open('知乎聚类分析/zhihuque.txt', 'r', encoding='utf-8') as fp:
    for d in fp:
        text_list.append(d)

# TfidfVectorizer可以把原始文本转化为TF-IDF的特征矩阵
tfidf_matrix = tfidf_vectorizer.fit_transform(text_list)

'''
n_clusters: 指定K的值
max_iter: 对于单次初始值计算的最大迭代次数
n_init: 重新选择初始值的次数
init: 制定初始值选择的算法
n_jobs: 进程个数，为-1的时候是指默认跑满CPU
注意，这个对于单个初始值的计算始终只会使用单进程计算，
并行计算只是针对与不同初始值的计算。比如n_init=10，n_jobs=40, 
服务器上面有20个CPU可以开40个进程，最终只会开10个进程
'''
num_clusters = 10
km_cluster = KMeans(n_clusters=num_clusters,max_iter=300, n_init=1,init='k-means++',n_jobs=1)

#返回各自文本的所被分配到的类索引
result = km_cluster.fit_predict(tfidf_matrix)
print ("Predicting result: ", result)
