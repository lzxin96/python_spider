import requests

# 不使用Session对象发送请求，其中set/name/Bill相当于向服务端写入一个名为name的Cookies
# 值为Bill
requests.get('http://httpbin.org/cookies/set/name/Bill')
# 第2次发送请求，这2次请求不在同一个Session中，第1次请求发送的Cookie在第2次请求中是无法获得的
r1 = requests.get('http://httpbin.org/cookies')
print(r1.text)

# 使用Session
# 创建Session对象
session = requests.Session()
# 第1次发送请求
session.get('http://httpbin.org/cookies/set/name/Bill')
# 第2次发送请求
r2 = session.get('http://httpbin.org/cookies')
print(r2.text)