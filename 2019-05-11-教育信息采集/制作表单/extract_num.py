import re

string = '(205)建筑工程学院'

num = re.search('\((\d+)\)(.*?)$', string).group(1)
string = re.search('\((\d+)\)(.*?)$', string).group(2)
print(result_1)
print(result_2)
