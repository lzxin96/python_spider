import requests
# 访问淘宝首页
r = requests.get('https://www.taobao.com')
# 输出get方法返回值类型
print(type(r))
# 输出状态码
print(r.status_code)
# 输出响应体类型
print(type(r.text))
# 输出Cookie
print(r.cookies)
# 输出响应体
# print(r.text)