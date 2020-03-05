#! usr/bin/python
# -*- coding: utf-8 -*-
'''
@user: sean
@project_name:project
@file_name:demo_02 
@date:2019/5/6
'''

import pandas as pd

data = {}
with open('cut_result.txt', 'r', encoding='utf-8') as f1, open('cut_stop_word.txt', 'r', encoding='utf-8') as f2:
    result = [i.strip() for i in f1.readlines()]
    text = [i.strip() for i in f2.readlines()]
    data['label'] = result
    data['position'] = text


data = pd.DataFrame(data)
data.to_csv('cut_result.csv', index=False)