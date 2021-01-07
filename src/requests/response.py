import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
}

# 向简书发送GET请求
r = requests.get('http://www.jianshu.com', headers=headers)
# 输出状态码
print(type(r.status_code),r.status_code)
# 输出响应头
print(type(r.headers),r.headers)
# 输出Cookie
print(type(r.cookies),r.cookies)
# 输出请求的URL
print(type(r.url),r.url)
# 输出请求历史
print(type(r.history), r.history)
# 根据codes中的值判断状态码
# codes对应文件在requests根目录中status_codes.py
if not r.status_code == requests.codes['ok']:
    print("failed")
else:
    print("ok")