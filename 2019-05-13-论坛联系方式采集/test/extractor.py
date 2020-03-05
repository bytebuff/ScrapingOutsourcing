# -*- coding: utf-8 -*-
import re, string
from itertools import groupby


class Extractor(object):

    def __init__(self):
        # 中文的标点符号
        self.chinese_punctuation = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."

    def extract_emails(self, text):
        """
        从文本中提取邮箱地址  提取的是英文邮箱地址 地址中不包含中文 会先去除中文  然后选择邮箱
        eg: extract_email('我的email是ifee@baidu.com和dsdsd@dsdsd.com,李林的邮箱是eewewe@gmail.com哈哈哈')
        :param: raw_text
        :return: 返回邮箱地址列表<list>
        """
        if text=='':
            return []
        eng_texts = self.replace_chinese(text) # 去除所有中文字符
        sep = ',!?:：; ，。！？《》、|\\/\n'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        # print(eng_split_texts)
        email_pattern = r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

        emails = []
        for eng_text in eng_split_texts:
            result = re.match(email_pattern, eng_text, flags=0)
            if result:
                emails.append(result.string)
        return list(set(emails)) # 返回去重后的数据

    def extract_ids(self, text):
        """
        extract all ids from texts<string>
        eg: extract_ids('my ids is 150404198812011101 m and dsdsd@dsdsd.com,李林的邮箱是eewewe@gmail.com哈哈哈')
        :param: raw_text
        :return: ids_list<list>
        """
        if text == '':
            return []
        eng_texts = self.replace_chinese(text)
        sep = ',!?:; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele) == 18]

        id_pattern = r'^[1-9][0-7]\d{4}((19\d{2}(0[13-9]|1[012])(0[1-9]|[12]\d|30))|(19\d{2}(0[13578]|1[02])31)|(19\d{2}02(0[1-9]|1\d|2[0-8]))|(19([13579][26]|[2468][048]|0[48])0229))\d{3}(\d|X|x)?$'

        phones = []
        for eng_text in eng_split_texts_clean:
            result = re.match(id_pattern, eng_text, flags=0)
            if result:
                phones.append(result.string.replace('+86','').replace('-',''))
        return list(set(phones)) # 返回去重后的数据

    def replace_chinese(self, text):
        """
        去除文本中所有的汉字
        eg: replace_chinese('我的email是ifee@baidu.com和dsdsd@dsdsd.com,李林的邮箱是eewewe@gmail.com哈哈哈')
        :param: raw_text
        :return: text_without_chinese<str>
        """
        if text=='':
            return []
        filtrate = re.compile(u'[\u4E00-\u9FA5]')
        text_without_chinese = filtrate.sub(r' ', text)
        return text_without_chinese

    def extract_cellphones(self, text):
        """
        extract all cell phone numbers from texts<string>
        eg: extract_email('my email address is sldisd@baidu.com and dsdsd@dsdsd.com,李林的邮箱是eewewe@gmail.com哈哈哈')
        :param: raw_text
        :return: email_addresses_list<list>
        """
        if text=='':
            return []
        eng_texts = self.replace_chinese(text)
        sep = ',!?:：; ：，.。！？《》、|\\/\n' + string.ascii_letters
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele)>=7 and len(ele)<17]

        phone_pattern = r'^((\+86)?([- ])?)?(|(13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9])|(19[0-9]))([- ])?\d{3}([- ])?\d{4}([- ])?\d{4}$'

        phones = []
        for eng_text in eng_split_texts_clean:
            result = re.match(phone_pattern, eng_text, flags=0)
            if result:
                phones.append(result.string.replace('+86','').replace('-',''))
        return list(set(phones)) # 返回去重后的数据


    def replace_cellphoneNum(self, text):
        """
        remove cellphone number from texts. If text contains cellphone No., the extract_time will report errors.
        hence, we remove it here.
        eg: extract_locations('我家住在陕西省安康市汉滨区，我的手机号是181-0006-5143。')
        :param: raw_text<string>
        :return: text_without_cellphone<string> eg: '我家住在陕西省安康市汉滨区，我的手机号是。'
        """
        eng_texts = self.replace_chinese(text)
        sep = ',!?:：; ：，.。！？《》、|\\/\n' + string.ascii_letters
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele)>=7 and len(ele)<17]
        for phone_num in eng_split_texts_clean:
            text = text.replace(phone_num,'')
        return text

    def replace_ids(self, text):
        """
        remove cellphone number from texts. If text contains cellphone No., the extract_time will report errors.
        hence, we remove it here.
        eg: extract_locations('我家住在陕西省安康市汉滨区，我的身份证号是150404198412011312。')
        :param: raw_text<string>
        :return: text_without_ids<string> eg: '我家住在陕西省安康市汉滨区，我的身份证号号是。'
        """
        if text == '':
            return []
        eng_texts = self.replace_chinese(text)
        sep = ',!?:：; ：，.。！？《》、|\\/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]
        eng_split_texts_clean = [ele for ele in eng_split_texts if len(ele) == 18]

        id_pattern = r'^[1-9][0-7]\d{4}((19\d{2}(0[13-9]|1[012])(0[1-9]|[12]\d|30))|(19\d{2}(0[13578]|1[02])31)|(19\d{2}02(0[1-9]|1\d|2[0-8]))|(19([13579][26]|[2468][048]|0[48])0229))\d{3}(\d|X|x)?$'
        ids = []
        for eng_text in eng_split_texts_clean:
            result = re.match(id_pattern, eng_text, flags=0)
            if result:
                ids.append(result.string)

        for phone_num in ids:
            text = text.replace(phone_num,'')
        return text

    def extract_wechats(self, text):
        """
        从文本中提取微信账号
        :param: raw_text
        :return: 返回微信<list>
        """
        if text=='':
            return []
        eng_texts = self.replace_chinese(text) # 去除所有中文字符
        sep = ',!?:：; ，。！？《》、|\\/\n'
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]

        wechat_pattern = r'^[a-zA-Z][a-zA-Z\d_-]{5,20}$'

        wechats = []
        for eng_text in eng_split_texts:
            result = re.match(wechat_pattern, eng_text, flags=0)
            if result:
                wechats.append(result.string)
        return list(set(wechats)) # 返回去重后的数据

    def extract_qqs(self, text):
        """
        从文本中提取qq
        :param: raw_text
        :return: 返回微信<list>
        """
        if text=='':
            return []
        eng_texts = self.replace_chinese(text) # 去除所有中文字符
        sep = self.chinese_punctuation + string.ascii_letters + string.punctuation + string.whitespace
        eng_split_texts = [''.join(g) for k, g in groupby(eng_texts, sep.__contains__) if not k]

        qq_pattern = r'^[1-9][0-9]{4,10}$'

        qqs = []
        for eng_text in eng_split_texts:
            result = re.match(qq_pattern, eng_text, flags=0)
            if result:
                qqs.append(result.string)
        return list(set(qqs)) # 返回去重后的数据



if __name__ == '__main__':

    text = '''
    急寻特朗普，男孩，于2018年11月27号11时在陕@西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：181 0006 5143，166-6156-2938，哈哈baizhantang@sina.com.cn 和yangyangfuture at gmail dot com
    急寻特朗普，男孩，于2018年11月27号11时在陕@西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：181 0006 5143，132-6156-2938，哈哈baizhantang@sina.com.cn 和yangyangfuture at gmail dot com
    急寻特朗普，男孩，于2018年11月27号11时在陕@西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：181 0006 5143，132-6156-2938，哈哈baizhantang@sina.com.cn 和yangyangfuture at gmail dot com
  
    Powered by D1scuz!  © 2001-2020 FOBShanghai.com 
    Processed in 0.261158 second(s), 8 queries , Gzip enabled ,243	TOP
    清除 Cookies - 联系我们 - 福步外贸网 - Archiver - 手机WAP版 - 手机客户端 RSS 订阅全部论坛 ..
    '''
    extractor = Extractor()

    # 提取邮箱地址
    emails = extractor.extract_emails(text)
    print(emails)

    # 提取手机号
    cellphones = extractor.extract_cellphones(text)
    print(cellphones)

    # 提取身份证号
    ids = extractor.extract_ids('my ids is 150404198812011101 m and dsdsd@dsdsd.com,李林的邮箱是eewewe@gmail.com哈哈哈')
    print(ids)

    # 提取微信
    wechats = extractor.extract_wechats(text)
    print(wechats)

    # 提取QQ号
    qqs = extractor.extract_qqs(text)
    print(qqs)