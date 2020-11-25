import http.cookiejar, urllib.request

filename = 'D:/py_space/spider/python_spider/src/urllib/cookies.txt'
cookie = http.cookiejar.LWPCookieJar()
# 装载cookies.txt文件，由于使用LWPCookieJar读取Cookie，所以Cookies文件必须是LWP格式
cookie.load(filename, ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://127.0.0.1:5000/readCookie')
# for item in cookie:
#     print(item.name + '=' + item.value)
print(response.read().decode('utf-8'))