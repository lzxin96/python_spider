from bs4 import BeautifulSoup

html = '''
<html>
    <head><title>这是一个演示页面</title></head>
    <body>
        <a href='a.html'>第一页</a>
        <p>
        <a href='b.html'>第二页</a>
    </body>
</html>
'''
# 创建BeautifulSoup对象，并通过BeautifulSoup类的第2个参数指定lxml解析器
soup = BeautifulSoup(html, 'lxml')
# 获取<title>标签的文本
print('<' + soup.title.string + '>')
# 获取第1个<a>标签的href属性值
print('[' + soup.a["href"] + ']')
print('[' + soup.a["href"] + ']')
# 以格式化后的格式输出这段HTML代码
print(soup.prettify())