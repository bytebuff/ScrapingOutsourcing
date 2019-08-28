#! usr/bin/python
# -*- coding: utf-8 -*-
'''
@user: sean
@project_name:project
@file_name:demo_03 
@date:2019/5/14
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


# data = pd.read_csv('result2.csv', encoding='gbk')
# data_9 = data[data['label'] == 9.0]
# data_9 = data_9.dropna()
# data_9 = data_9.groupby('money').count().reset_index()
# data_9.to_csv('money.csv', encoding='utf8', index=False)

# data_plt = data_9['money'].plot(kind='bar')
# plt.show()
# print(data_plt)

data_2 = pd.read_csv('money2.csv', encoding='gbk')
# print(data_2)
plt.figure(figsize=(10, 8))
sns.barplot(x=data_2['money'], y=data_2['label'])
plt.savefig('test.jpg')
plt.show()