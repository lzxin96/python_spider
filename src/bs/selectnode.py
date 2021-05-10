from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup演示</title>
</head>
<body>
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item4" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item5"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'lxml')
# 获取title节点的名称
print(soup.title.name)
# 获取第1个li节点的所有属性名和属性值
print(soup.li.attrs)
# 获取第1个li节点value2的属性的值
print(soup.li.attrs['value2'])
# 获取第1个li节点value1属性的值
print(soup.li['value1'])
# 获取第1个a节点的href属性值
print(soup.a['href'])
# 获取第1个a标签的文本内容
print(soup.a.string)