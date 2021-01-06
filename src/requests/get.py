import requests
# 用字典定义GET请求参数
data = {
    'name':'Bill',
    'country':'中国',
    'age':20
}
# 发送HTTP GET请求
# params参数以字典的方式在url中加入参数。
# 参数名相同，值同则为同一个参数；值不同则以列表的方式按先后出现顺序存储
r = requests.get('http://httpbin.org/get?name=Mike&country=美国&age=40', params=data)
# 输出响应体
print(r.text)
# 将返回对象转换为json对象
print(r.json())
# 输出json对象中的country属性值，会输出一个列表，因为有2个GET请求参数的名字都是country
print(r.json()['args']['country'])