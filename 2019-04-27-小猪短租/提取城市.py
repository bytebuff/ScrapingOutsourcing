import re



with open(r'小猪短租\citys.txt', encoding='utf-8') as fp:
    all_citys = {}
    for line in fp:
        #line = re.findall("new Array('(.*?)','(.*?)',", line)
        if not line == '\n':
            data = line.strip()
            # print(data)
            short, city_name = re.findall("Array\('(.*?)','(.*?)',", data)[0]
            city = [(city_name, short)]
            city = dict(city)
            all_citys.update(city)
    