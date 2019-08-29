# 0. 导入模块 用来打开字体文件 将字体文件转化成其他格式 XML
# 第三方模块 pip install 安装
from fontTools.ttLib import TTFont
import requests # pip 
import re

# 1. 将字体文件加载进来 采用TTFont加载进来
font = TTFont('iconfont_9eb9a50.woff')

# 2. 将woff文件转化成XML文件, saveXML
# font.saveXML('iconfont.xml')

# 3. 选择出cmap 编码映射表
best_cmap = font['cmap'].getBestCmap()

# 4. 将编码映射表的键转化成16进制
new_best_cmap = {}  # 字典格式
for key, value in best_cmap.items():  # 返回 键  值
    # print(key, value)
    key = hex(key)
    new_best_cmap[key] = value
# print(new_best_cmap)

# 5. 将num_x和数字对应起来
num_cmap = {
    'x': '', 'num_': '1', 'num_1': '0',
    'num_2': '3', 'num_3': '2',
    'num_4': '4', 'num_5': '5',
    'num_6': '6', 'num_7': '9',
    'num_8': '7', 'num_9': '8'
}

# 6. 将num_对应的数字和16进制的对应起来
new_num_map = {} # 存放数字和16进制
for key, value in new_best_cmap.items():
    if value in num_cmap:
        new_num_map[key] = num_cmap[value]
print(new_num_map)

# 7. 请求得到网页信息
## 请求源码
url = 'https://www.iesdouyin.com/share/user/88445518961?timestamp=1548046967'
# 添加请求头信息
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'}
# 请求网址资源
response = requests.get(url, headers=header)
# 提取响应信息
text = response.text # 文本信息

# 8. 将网页信息替换成具体的数字
for font_key, font_value in new_num_map.items():
    # print(font_key, font_value)
    # 替换0--->&#
    font_key = re.sub('0', '&#', font_key, count=1)
    # 将;也替换掉
    font_key = f'{font_key};' # font_key = font_key+';'
    # 将源码中的键值替换成数字
    if font_key in text: # 判断是否存在
        # re.sub 替换
        text = re.sub(font_key, font_value, text)

# 9. 保存替换后的信息  用来检查是否替换成功了
with open('douyin.html', 'w', encoding='utf-8') as fp:
    fp.write(text)