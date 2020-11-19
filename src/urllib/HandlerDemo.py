from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# 创建ProxyHandler对象，并指定HTTP和HTTPS代理的IP和端口号
proxy_handler = ProxyHandler({
    'http':'代理ip',
    'https':'代理ip'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://www.jd.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
