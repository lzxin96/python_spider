from urllib import request
from urllib.parse import unquote,urlencode
import base64

url = 'http://httpbin.org/post'# Request类构造方法必须参数
header = {
    'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Host':'httpbin.org',
    # 设置中文http请求头，用url编码格式（字典）
    'chinese1':urlencode({'name':'李宁'}),# http请求头只支持处理英文字符和符号
    # 设置中文http请求头，用bese64格式(byte)
    'MyChinese':base64.b64encode(bytes('这是中文http请求头', encoding='utf-8')),
    'who':'python Scrapy'
}
dict = {
    'name':'Bill',
    'age':'30'
}
data = bytes(urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=header, method='POST')
# 通过add_header方法添加中文http请求头，url编码格式
req.add_header('Chinese2', urlencode({'国籍':'中国'}))
response = request.urlopen(req)

# 获取并解码服务端的响应信息
value = response.read().decode('utf-8')
print(value)

import json
# 将返回值转换为json对象
responseObj = json.loads(value)
# 解码url编码格式的http请求头
print(unquote(responseObj['headers']['Chinese1']))
# 解码url编码格式的http请求头
print(unquote(responseObj['headers']['Chinese2']))
# 解码base64编码格式的http请求头
print(str(base64.b64decode(responseObj['headers']['Mychinese']), 'utf-8'))