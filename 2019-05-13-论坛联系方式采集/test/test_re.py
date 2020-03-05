import re
text = "Pl Weichat: chenjack2008 ease16639402460 contact us 1960958490@qq.com.cn at contact@qq.com for further information."+\
        " You can also give 26698457820feedbacl at feedback@yiibai.com 13298307816 as "

text2 = '''
本人，常住在福建莆田，有多年外贸行业、卖家和第三方验货工作经验。目前有5个人小团队。

承接福建区域 ( 宁德，南平，福州，福清，莆田，泉州，晋江，德化，厦门 等）， 浙江温州温岭区域，广东潮汕一带的验货与货柜监装或者验厂， 擅长于（Softline/Hardline）鞋类、箱包，服装，面料，陶瓷, 竹制品, 卫浴，五金，圣诞礼品 等验货监柜验厂服务。

自带电脑，数码相机，卡尺等所需要的验货工具，经验丰富，工作守约，诚信，谦虚，专业，热情，可靠，当天可出中英文报告或者依据客人要求出具报告。
            
Jack Chen
QQ: 664122715
Weichat: chenjack2008  13799676355
E-mail: chenjack2008@126.com
Tel: +86 13799676355
'''

# emails = re.findall("\w+[-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*", text2)
# phones = re.findall(r'[1]+[3,5,6,7,8]+\d{9}', text2) # 手机号码
# qqs = re.findall(r'[1-9][0-9]{4,10}', text2)
# wechats = re.findall('[a-zA-Z]{1}[-_a-zA-Z0-9]{5,19}', text2)

# print(emails)
# print(phones)
# print(qqs)
# print(wechats)


from itertools import groupby

eng_texts = '''Tel: *+86,137 9967 6355'''
sep = ',+' # 根据引号里面的内容切割文本 保留切割用的字符以及文本  也就是引号里面的
for k, g in groupby(eng_texts, sep.__contains__):
    print(k, '-->', ''.join(g))