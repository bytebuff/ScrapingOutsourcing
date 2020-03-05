import requests

url = 'https://www.google.com.hk/search?q=%E5%9B%BD%E5%AD%A6%E5%9F%B9%E8%AE%AD&safe=strict&ei=2vWVXNH_OOvVmAWD1p-QCQ&start=60&sa=N&ved=0ahUKEwjR1M-185fhAhXrKqYKHQPrB5I4FBDy0wMIbg&biw=1366&bih=635'

DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cookie': 'CGIC=InZ0ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSxpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIz; NID=164=Xy0D8yL4ZYjNoFGtUbkxOnm9jvBxX3Bqp6lcPJnWFyeUjY64FuFoek97HpjPZ8PfWWJv-gOix0aLBAX7Xi1FyIg6k7MNdFC1GstX0UDJ9J7K6em7r8vS9GUM1EPH-evfrzpWyEOCNczAyRj9Xzwn7lmwBWeL_aSxQyn_0q2OnKSpMjUHEvE; DV=o0oM2iCJgOct0J-HU_sc0efC3oecmpb9oYQs_p7gpQEAAAA; ANID=AHWqTUmuMtwMvaMxEntZjwbJRYMmEQv8tmvY-BqAhuqeuxJsoZ66dGJBh95VnHoi; 1P_JAR=2019-3-23-9',
    'referer': 'https://www.google.com.hk/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'x-client-data': 'CK+1yQEIibbJAQijtskBCMG2yQEIqZ3KAQioo8oBCLGnygEI4qjKAQ==',
}

response = requests.get(url, headers=DEFAULT_REQUEST_HEADERS)

print(response.text)
