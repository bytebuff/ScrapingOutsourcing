import requests
import re, json, pandas, os
from urllib.request import urlretrieve


url = 'http://www.shihuo.cn/sports/detail/60725.html#qk=list'
# url = 'http://www.shihuo.cn/sports/detail/407.html#qk=list'


def parseD(url):
    # 解析数据 保存数据
    res = requests.get(url)

    goodInfo = re.findall(pattern="goods_info = (.*?)',", string=res.text)[0]
    info1 = goodInfo.replace(r'\x22','"').replace(r"\\\/",r'/').replace(r'\\','\\').replace('/\\','\\').replace("'",'')
    js1 = json.loads(info1) # 获取json格式的数据
    content = js1['content']
    brand = js1['brand']
    nameD = js1['name']
    series = js1['series']
    category = js1['category']
    #print(content)
    # 商品图片和颜色的名字
    goodStyle = re.findall(pattern="goods_styles = (.*?)',", string=res.text)[0]
    info2 = goodStyle.replace(r'\x22','"').replace(r"\\\/",r'/').replace(r'\\','\\').replace('/\\','\\').replace("'",'')
    print(info2)
    js2 = json.loads(info2) # 获取json格式的数据
    #print(js2)

    for style in js2:
        # data = f'{category}, {name}, {content}, {sizes}, {style_id}, {style_url}'
        # data = [(category, name, content, sizes, style_id, style_url)]

        #print(style)
        # content 评论内容
        # brand  品牌名字
        # category 分类
        name = style['name'] # 颜色
        size = style['size'] # 尺寸
        value = style['value'] # 图片

        data = [(category, brand, nameD, series, name, size, content, value)]
        print(data)

        data = pandas.DataFrame(data)
        data.to_csv('xiuxian.csv', mode='a+', index=False, header=False)

        pat_h = f'./{category}/{brand}/{nameD}/{name}'
        # 创建文件夹
        if not os.path.exists(pat_h):

            try:
                picture_path = os.makedirs(pat_h)
            except:
                pass

        for pic in value:
            pic = f'http:{pic}'
            print(pic)
            respic = requests.get(pic)
            pic_name = re.split('/', pic)[-1]
            print(pic_name)
            # C:\Users\19609\Desktop\工作相关\公开课
            # urlretrieve(pic,filename=pat_h)
            try:

                with open(f'{pat_h}/{pic_name}', 'wb') as fp:
                    fp.write(respic.content)

            except:
                pass

if __name__ == '__main__':

    parseD(url)