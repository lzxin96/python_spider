import urllib.request
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        # 进行异常处理，这里只是简单地输出了“超时”，在真实情况可以进行更加复杂的处理
        print('超时')
# 在这里可以继续爬虫工作
print('继续爬虫其他工作')
