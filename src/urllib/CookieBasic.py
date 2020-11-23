# 获取cookie
import http.cookiejar, urllib.request

# 创建CookieJar对象
cookie = http.cookiejar.CookieJar()
# 创建HTTPCookieProcessor对象
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# 给http://baidu.com发送请求,并获取相应数据
response = opener.open('http://baidu.com')
print('-------------http://baidu.com-------------')

# 输出服务端发送的所有Cookie
for item in cookie:
    print(item.name + '=' + item.value)
print('-------http://127.0.0.1:5000/writeCookie-------')

# 下面的代码用同样的方式访问CookieServer,并输出返回的Cookie
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://127.0.0.1:5000/writeCookie')
for item in cookie:
    print(item.name + '=' + item.value)