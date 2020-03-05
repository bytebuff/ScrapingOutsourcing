import requests

# # 采集城市
# city_url = 'https://yz.chsi.com.cn/zsml/pages/getSs.jsp'
# # 采集城市的代码
# response = requests.post(city_url, data='')
# print(response.json())
# with open('city.txt', 'w', encoding='utf-8') as fp:
#     fp.write(response.text)

city_data = [{"mc":"北京市","dm":"11"},
             {"mc":"天津市","dm":"12"},
             {"mc":"河北省","dm":"13"},
             {"mc":"山西省","dm":"14"},
             {"mc":"内蒙古自治区","dm":"15"},
             {"mc":"辽宁省","dm":"21"},
             {"mc":"吉林省","dm":"22"},
             {"mc":"黑龙江省","dm":"23"},
             {"mc":"上海市","dm":"31"},
             {"mc":"江苏省","dm":"32"},
             {"mc":"浙江省","dm":"33"},
             {"mc":"安徽省","dm":"34"},
             {"mc":"福建省","dm":"35"},
             {"mc":"江西省","dm":"36"},
             {"mc":"山东省","dm":"37"},
             {"mc":"河南省","dm":"41"},
             {"mc":"湖北省","dm":"42"},
             {"mc":"湖南省","dm":"43"},
             {"mc":"广东省","dm":"44"},
             {"mc":"广西壮族自治区","dm":"45"},
             {"mc":"海南省","dm":"46"},
             {"mc":"重庆市","dm":"50"},
             {"mc":"四川省","dm":"51"},
             {"mc":"贵州省","dm":"52"},
             {"mc":"云南省","dm":"53"},
             {"mc":"西藏自治区","dm":"54"},
             {"mc":"陕西省","dm":"61"},
             {"mc":"甘肃省","dm":"62"},
             {"mc":"青海省","dm":"63"},
             {"mc":"宁夏回族自治区","dm":"64"},
             {"mc":"新疆维吾尔自治区","dm":"65"},
             {"mc":"台湾省","dm":"71"},
             {"mc":"香港特别行政区","dm":"81"},
             {"mc":"澳门特别行政区","dm":"82"}]

# # 采集大类专业
# zhuanye_url = 'https://yz.chsi.com.cn/zsml/pages/getMl.jsp'
# # 采集大类专业的代码
# response_zhuanye = requests.post(zhuanye_url, data='')
# print(response_zhuanye.json())
i=0
zhuanye_data = [{'mc': '哲学', 'dm': '01'}, {'mc': '经济学', 'dm': '02'}, {'mc': '法学', 'dm': '03'}, {'mc': '教育学', 'dm': '04'}, {'mc': '文学', 'dm': '05'}, {'mc': '历史学', 'dm': '06'}, {'mc': '理学', 'dm': '07'}, {'mc': '工学', 'dm': '08'}, {'mc': '农学', 'dm': '09'}, {'mc': '医学', 'dm': '10'}, {'mc': '军事学', 'dm': '11'}, {'mc': '管理学', 'dm': '12'}, {'mc': '艺术学', 'dm': '13'}]

for city in city_data:
    for zhuanye in zhuanye_data:
        # print(city, zhuanye)
        xiaozhuanye_url = 'https://yz.chsi.com.cn/zsml/pages/getZy.jsp'
        data = {
            'mldm': zhuanye.get('dm')
        }
        try:
            response_xiaozhuanye = requests.post(xiaozhuanye_url, data=data, timeout=60)
        except:
            pass


        for xiaozhuanye in response_xiaozhuanye.json():
            # print(xiaozhuanye)
            xxiaozhuanye_url = 'https://yz.chsi.com.cn/zsml/code/zy.do'
            data = {
                'q': xiaozhuanye.get('dm')
            }
            try:
                response_xxiaozhuanye = requests.post(xxiaozhuanye_url, data=data, timeout=60)
            except:
                pass

            try:
                d = response_xxiaozhuanye.json()
            except:
                d = []
            for xx in d:

                data = {
                    'ssdm': city.get('dm'),
                    'dwmc': '',
                    'mldm': zhuanye.get('dm'),
                    'mlmc': '',
                    'yjxkdm': xiaozhuanye.get('dm'),
                    'zymc': xx,
                    'xxfs': ''
                }
                print(data)

                # u = 'https://yz.chsi.com.cn/zsml/queryAction.do'
                # response = requests.post(u, data=data)
                # print(response.text)
                try:
                    with open('post_data.txt', 'a', encoding='utf-8') as fp:
                        fp.write(str(data)+'\n')
                except:
                    i= i + 1
                    print(f'出错{i}')