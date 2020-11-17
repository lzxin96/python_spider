import urllib.request
# 向京东商城发送http get 请求，urlopen函数既可以使用http，也可以使用https
response = urllib.request.urlopen('https://wwww.jd.com')
# 输出urlopen的函数返回值的数据类型
print('response的类型：', type(response))
# 输出相应状态码、相应消息和http版本
print('status:', response.status, 'msg:', response.msg, 'version:', response.version)
# 输出所有的响应头信息
print('headers:', response.getheaders())
# 输出名为Content-Type的响应头信息
print('header.Content-type:', response.getheader('Content-Type'))
# 输出京东商城首页所有的HTML代码（经过utf-8解码）
print(response.read().decode('utf-8'))