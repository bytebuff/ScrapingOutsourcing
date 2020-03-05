import os, codecs
import jieba
from collections import Counter


def get_words(txt):
    seg_list = jieba.cut(txt)
    counter = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            counter[x] += 1
    print('常用词频度统计结果')
    for (k, v) in counter.most_common(100):
        print('%s%s %s  %d' % ('\t' * (5 - len(k)), k, '*' * int(v / 3), v))


if __name__ == '__main__':
    with codecs.open('19d.txt', 'r', 'utf8') as f:
        txt = f.read()
        get_words(txt)
