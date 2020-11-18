from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError
username = 'bill'
password = '1234'
url = 'http://localhost:5000'

p = HTTPPasswordMgrWithDefaultRealm()
# 封装realm, url和用户名、密码
# 第一个参数realm，若指定则需与服务器端WWW-Authenticate字段指定的realm一致
p.add_password('localhost', url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
# 发送HTTP请求
opener = build_opener(auth_handler)
# try防止realm不一致导致程序奔溃
try:
    result = opener.open(url)
    # 获取服务器端相应数据
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


