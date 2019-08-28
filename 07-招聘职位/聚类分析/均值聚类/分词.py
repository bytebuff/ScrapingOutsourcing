import jieba
import csv, sys


def get_csv_file_to_line():

    try:
        file=open('运维.csv','r', encoding='utf-8')  #打开文件
    except FileNotFoundError:
        print('文件不存在')
    else:
        stus=csv.reader(file) # 读取文件内容
        for stu in stus:  # 一行是一个数组
            # print(stu[0])  # 取每个数组的第一个元素
            yield stu[0]

def jieba_cut():

    f = open('36krout.txt', 'r', encoding='utf-8')
    dataset = []
    for line in f.readlines():
        line = jieba.cut(line)
        line = '\n'.join(line)
    f.close()
    return dataset


# 创建停用词列表
def stop_words_list():
    stopwords = [line.strip() for line in open('stop_words.txt',encoding='UTF-8').readlines()]
    return stopwords


def save_to_file(data):
    with open('cut_stop_word.txt','a', encoding='utf-8') as fp:
        fp.write(data+'\n')


if __name__ == '__main__':
    csv_lines = get_csv_file_to_line()
    stop_words = stop_words_list()

    # 添加自定义单词
    jieba.add_word('大数据', freq=sys.maxsize)
    jieba.add_word('云计算', freq=sys.maxsize)

    print('停用词-->', stop_words)

    for line in csv_lines:
        line = jieba.cut(line)
        line = list(line)
        stoped_words = [item for item in line if item not in stop_words]
        print(stoped_words)
        words = ','.join(stoped_words)
        save_to_file(words)

