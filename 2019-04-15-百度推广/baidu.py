import requests

url = 'https://fengchao.baidu.com/hairuo/request.ajax'

headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    #'content-length': '343',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'BAIDUID=CDF0BA374A65DD45885EF8E1813F48C4:FG=1; PSTM=1553774085; BDUSS=hxWndPZEZiVnJNQnZ1TWRKMzBtOGpnTS05aGR6bX56bnFHbzl-bENYU0tqTk5jRVFBQUFBJCQAAAAAAAAAAAEAAABSO6NAyrfC87jqZmx5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIr~q1yK~6tcbF; BIDUPSID=A67769B22B567920155B2DEF7489595B; BCLID=10762817780612159563; BDSFRCVID=_QKOJeC629EWIX59R23hKkp_OeJ7hDQTH6aoORHX0B4bAqd-uUzTEG0PDM8g0KubhaS4ogKKXgOTHw0F_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tRAOoCD-tKvjDb7GbKTD-tFO5eT22-usXK3C2hcH0KLKJM86hlu5ej0iQxbtKU3rWITDBhrHJMb1MRjveMnoXTK3-x52bTchLbc3bq5TtUJaJKnTDMRhqqJXe-jyKMniyIv9-pn5tpQrh459XP68bTkA5bjZKxtq3mkjbIOFfDDbbDtmej_35n-Wql6354Rj2C_X3b7Eq-OEeKClD6LaDjJbDa-h-R3LX57yL4oJ5C6DHJTg5J3jKbTE5qOLy-r-5I5tWC6J-P-3b-oeKU6qLUtbQNbJJh3ZfRnkWhjlaRRRJtQ8Mt6I0JJ--HQ-JMIEtJPDVI82JCD3j-5cbjAWq4tehHRdQxn9WDTm_D_X3x3zoKKw06K5MMPfKbn9KxIf2gnI-pPKKR7cVlnyDMKM-x_Lb2ctLRTn3mkjbpbzfn02OP5PM-Q6j-4syPRvKMRnWTkjKfA-b4ncjRcTehoM3xI8LNj405OTt2LE3-oJqC_hMI_R3H; PSINO=3; delPer=0; H_PS_PSSID=1430_21089_18560_20697_28772_28721_28557_28834_28584_28640_26350_28519; uc_login_unique=d4fae03cf079fe939a98185f5929d32a; uc_recom_mark=cmVjb21tYXJrXzI0MjA0Mjk2; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a03053311533; __cas__st__3=70e099aca72bc52b9205702e7355f6efbcaa60e0de733c1cd4f00c9ed0cd3cfbcde424d8b8351f19c70e0e36; __cas__id__3=24204296; __cas__rn__=305331153; CPTK_3=1136848554; CPID_3=24204296; COOKIE_SESSION=0_0_0_0_0_0_0_0_0_0_0_0_0_1555318883%7C1%230_0_0_0_0_0_0_0_1555318883%7C1; lsv=globalTjs_3aec804-wwwTcss_159649e-wwwTcss_159649e-wwwBcss_020c45a-framejs_90e3ff2-atomentryjs_689bd71-globalBjs_fe64ae8-sugjs_2c6c63d-wwwjs_d544348',
    'origin': 'https://fengchao.baidu.com',
    'referer': 'https://fengchao.baidu.com/fc/manage/tools/user/24204296/adpreview',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

with open(r'C:\Users\19609\Desktop\SpiderEnv\百度推广\关键词.txt', 'r', encoding='utf-8') as fp:
    for line in fp:
        keyword = line.strip()
        data = {
            #'reqid': '4b534c47-b653-485b-43f1-155531907873',
            #'eventId': '4b534c47-3100-44dd-fb68-155531907867',
            'userid': '24204296',
            'token': '1136848554',
            'path': 'vane/GET/PromotionLiveService/processHumanRequest',
            'params': '{"keyword":"%s","device":1,"region":28226,"pageNo":0,"isHtml5Enable":true}'%keyword,
        }

        response = requests.post(url, data=data, headers=headers)

        print(response.text)

        with open(f'C:\\Users\\19609\\Desktop\\SpiderEnv\\百度推广\\{keyword}.txt','w',encoding='utf-8') as fp:
            fp.write(response.text)