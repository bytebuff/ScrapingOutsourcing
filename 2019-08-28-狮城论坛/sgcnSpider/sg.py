import requests

url = 'https://bbs.sgcn.com/forum-1205-1.html'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'iZOJfd_c4f3_saltkey=wGS1gpje; iZOJfd_c4f3_lastvisit=1552998531; _ga=GA1.2.4560908.1553002134; iZOJfd_c4f3_home_readfeed=1553136285; UM_distinctid=1699e30d785168-0806b06d47731c-7a1b34-100200-1699e30d78618; iZOJfd_c4f3_forumdefstyle=1; iZOJfd_c4f3_pvi=1748289145; CNZZDATA1252988760=1225757104-1554028789-%7C1554028789; iZOJfd_c4f3_visitedfid=1205D234D220D1253D1223D15D253D1259D157D65; _gid=GA1.2.882648011.1554028802; PHPSESSID=ohitp4mep3jqmap81vpfpo16q6; iZOJfd_c4f3_viewid=tid_16316846; iZOJfd_c4f3_st_t=0%7C1554029096%7C703ed0ef4a70f76ab645ec49b247e24c; iZOJfd_c4f3_forum_lastvisit=D_1205_1554029096; iZOJfd_c4f3_st_p=0%7C1554029328%7Ccb713d5818ea250de8fb1e74c761a14d; iZOJfd_c4f3_sendmail=1; iZOJfd_c4f3_lastact=1554029329%09connect.php%09check',
    'Host': 'bbs.sgcn.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}

response = requests.get(url, headers=headers)

print(response.text)