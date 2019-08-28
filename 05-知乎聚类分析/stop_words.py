import jieba.analyse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

"""
       TF-IDF权重：
           1、CountVectorizer 构建词频矩阵
           2、TfidfTransformer 构建tfidf权值计算
           3、文本的关键字
           4、对应的tfidf矩阵
"""

# 读取文件
def read_news():
    news = open('知乎聚类分析/zhihuque.txt','r',encoding='utf-8').read()
    return news


# jieba分词器通过词频获取关键词
def jieba_keywords(news):
    keywords = jieba.analyse.extract_tags(news, topK=10)
    print(keywords)

def tfidf_keywords():
    # 00、读取文件,一行就是一个文档，将所有文档输出到一个list中
    corpus = []
    for line in open('知乎聚类分析/zhihuque.txt', 'r', encoding='utf-8').readlines():
        corpus.append(line)

    # 01、构建词频矩阵，将文本中的词语转换成词频矩阵
    vectorizer = CountVectorizer()
    # a[i][j]:表示j词在第i个文本中的词频
    X = vectorizer.fit_transform(corpus)
    print(X)  # 词频矩阵

    # 02、构建TFIDF权值
    transformer = TfidfTransformer()
    # 计算tfidf值
    tfidf = transformer.fit_transform(X)

    # 03、获取词袋模型中的关键词
    word = vectorizer.get_feature_names()

    # tfidf矩阵
    weight = tfidf.toarray()

    # 打印特征文本
    print(len(word))
    for j in range(len(word)):
        print(word[j])

    # 打印权重
    for i in range(len(weight)):
        for j in range(len(word)):
            print(weight[i][j])

if __name__ == '__main__':
    news = read_news()
    jieba_keywords(news)
    # tfidf_keywords()
