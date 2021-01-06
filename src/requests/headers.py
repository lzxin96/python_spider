import requests
from urllib.parse import quote,unquote

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    # 将中文编码
    'name':quote('李宁')
}
# 发送HTTP GET请求
# 设置请求头headers参数
r = requests.get('http://httpbin.org/get', headers=headers)
# 输出响应体
print(r.text)
# 输出name请求头的值（需要解码）
print('Name', unquote(r.json()['headers']['Name']))