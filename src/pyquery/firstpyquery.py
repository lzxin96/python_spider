import pyquery
from pyquery import PyQuery as pq

html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
'''
# 方法一：使用字符串形式将HTML文档传入PyQuery对象
doc = pq(html)
# 输出<a>节点的将href属性值和文本内容
for a in doc('a'):
    print(a.get('href'), a.text)
# 方法二：使用URL形式将HTML文档传入PyQuery对象
doc = pq(url='https://www.jd.com')
# 输出页面的<title>节点的内容
print(doc('title'))

import requests
# 抓取HTML代码，并将HTML代码传入PyQuery对象
doc = pq(requests.get('https://www.jd.com').text)
print(doc('title'))
# 方法三：从HTML文件将HTML代码传入PyQuery对象
# filename = r'D:\py_space\spider\python_spider\src\pyquery\demo.html'
# open(filename, 'r', encoding='UTF-8') as f:
#     content = f.read()
# doc = pq(content)
doc = pq(filename=r'D:\py_space\spider\python_spider\src\pyquery\demo.html', decoding='UTF-8')
# 输出<head>节点的内容
print(doc('head'))