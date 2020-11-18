from urllib import request
import base64
url = 'http://localhost:5000'
headers ={
    'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Host':'localhost:5000',
    # 设置Authorization请求字段头，并指定Base64编码的用户名和密码
    'Authorization':'Base ' + str(base64.b64encode(bytes('bill:1234', 'utf-8')), 'utf-8')
}
req = request.Request(url=url, headers=headers, method="GET")
response = request.urlopen(req)
print(response.read().decode('utf-8'))