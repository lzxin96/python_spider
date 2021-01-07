import requests

# 指定data参数，字典类型
data = {
    'name':'Bill',
    'country':'中国',
    'age':20
}
# 向服务端发送POST请求
r = requests.post('http://httpbin.org/post', data=data)
# 输出响应体
print(r.text)
# 将返回对象转换为JSON对象
print(r.json())
# 输出表单中的country字段值
print(r.json()['form']['country'])