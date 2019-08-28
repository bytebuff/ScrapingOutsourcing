from aip import AipOcr


""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



def basicGeneralUrl(url):
    # 调用通用文字识别, 图片参数为本地图片
    return client.basicGeneralUrl(url)


if __name__ == '__main__':

    # get_picture('https://bbs.sgcn.com/code.php?LdleFF3bpn7MX6klcGAU8mQfKd4lK4v9X+wR++CgkXBsUgHL')
    # image = get_file_content('pic_66.png')
    # text = basicGeneral('https://bbs.sgcn.com/code.php?LdleFF3bpn7MX6klcGAU8mQfKd4lK4v9X+wR++CgkXBsUgHL')
    url = 'https://bbs.sgcn.com/code.php?INhHY6IhUM2K0Tiah1OgWy9DSvXmp9/Oy4aUgnZ8NwN7T6p/'
    text = basicGeneralUrl(url)
    print(text)
    if text.get('words_result', False):
        if text['words_result'][0:]:
            print(text['words_result'][0].get('words', None))
