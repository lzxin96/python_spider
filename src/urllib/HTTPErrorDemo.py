from urllib import request, error
import socket

try:
    response = request.urlopen("http://www.jd123.com/test.html")
except error.HTTPError as e: # 成功捕获Bad Request 异常
    print(type(e.reason))
    print(e.reason, e.code, e.headers)

try:
    response = request.urlopen("https://jd.com", timeout=0.00002)
except error.HTTPError as e: # 成功捕获time out 异常
    print('error.HTTPError:', e.reason)
except error.URLError as e: # 这里r.reason的类型是socket.timeout类
    print(type(e.reason))
    print('error.URLError:', e.reason)
    # 判断r.reason的类型是否为socket.timeout类
    if isinstance(e.reason, socket.timeout):
        print('超时错误')
    else:
        print('成功发送请求')
