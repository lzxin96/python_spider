import requests

print(type(open('Python从菜鸟到高手.png','rb')))
# 定义上传的文件，字典中必须有一个key为file的值，值类型是BufferedReader，可以用open函数返回
files1 = {'file':open('Python从菜鸟到高手.png','rb')}
# 将本地图像文件上传到upload_server.py
r1 = requests.post('http://127.0.0.1:5000', files=files1)
# 输出响应结果
print(r1.text)

files2 = {'file':open('Python从菜鸟到高手.png','rb')}
r2 = requests.post('http://httpbin.org/post',files=files2)
print(r2.text)