import http.cookiejar, urllib.request

filename1 = 'cookies1.txt'
filename2 = 'cookies2.txt'
# 创建MozillaCookieJar对象
cookie1 = http.cookiejar.MozillaCookieJar(filename1)
# 创建LWPCookieJar对象
cookie2 = http.cookiejar.LWPCookieJar(filename2)

handler1 = urllib.request.HTTPCookieProcessor(cookie1)
handler2 = urllib.request.HTTPCookieProcessor(cookie2)
opener1 = urllib.request.build_opener(handler1)
opener2 = urllib.request.build_opener(handler2)
opener1.open('http://www.csdn.net')
opener2.open('http://www.csdn.net')

# 将cookie保存为Mozilla格式
cookie1.save(ignore_discard=True, ignore_expires=True)
# 将cookie保存为LWP格式
cookie2.save(ignore_discard=True, ignore_expires=True)