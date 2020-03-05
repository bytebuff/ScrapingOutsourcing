'''
分析热门职位
'''
import requests # 网络请求
import re
import time
import random
import pandas as pd # 数据框操作
import numpy as np
import matplotlib.pyplot as plt # 绘图
import jieba # 分词
from wordcloud import WordCloud # 词云可视化
import matplotlib as mpl  # 配置字体
from pyecharts import Geo # 地理图


mpl.rcParams["font.sans-serif"] = ["SimHei"] # SimHei   Microsoft YaHei
# 配置绘图风格
plt.rcParams["axes.labelsize"] = 16.
plt.rcParams["xtick.labelsize"] = 14.
plt.rcParams["ytick.labelsize"] = 14.
plt.rcParams["legend.fontsize"] = 12.
plt.rcParams["figure.figsize"] = [15., 15.]

# 导入数据
data = pd.read_csv('XiAnData.csv', encoding='gbk')  # 导入数据
data.head()

final = {}
stopwords = ['工程师', '高级', '西安']  # 停止词
for n in range(data.shape[0]):

    seg_list = list(jieba.cut(data['岗位职称'][n]))

    for seg in seg_list:
        if seg not in stopwords:
            final[seg] = final.get(seg, 0) + 1
# final 得到的词频 按照大小排序

result = sorted(final.items(), key=lambda item: item[1])
print(result)
