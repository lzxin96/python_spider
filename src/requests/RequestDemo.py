from requests import Request,Session
# 打包请求
url = 'http://httpbin.org/post'
data = {
    'name':'Bill',
    'age':20
}
headers = {
    'country':'China'
}

session = Session()
# 1.封装请求数据,request中的Request类
req = Request('POST', url=url, data=data, headers=headers)
# 2.调用session.prepare_request，返回request.models.Request对象,预处理
prepared = session.prepare_request(req)
# 3.发送请求
r = session.send(prepared)
print(type(r))
print(r.text)