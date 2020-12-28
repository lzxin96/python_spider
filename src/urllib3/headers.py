from urllib3 import *
disable_warnings()
http = PoolManager()

url = 'http://www.baidu.com'
response = http.request('GET', url)
# 输出所有响应头字段和值
for key in response.info().keys():
    print(key, ':', response.info()[key])