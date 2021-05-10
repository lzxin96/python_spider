from bs4 import BeautifulSoup

html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup演示</title>
    <tag1><a><b></b></a></tag1>
</head>
<body>
<div>
    <ul>
        <li class="item1" value = "hello world">
            <a href="https://geekori.com"> 
                geekori.com
            </a>
        </li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
    </ul>
</div>
</body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
# 输出head的所有直接子节点
print(soup.head.contents)
print(soup.head.children)
print(type(soup.head.contents))
print(type(soup.body.div.ul.children))
print(type(soup.head.descendants))
# 对ul中的所有子节点进行迭代，并以文本形式输出子节点的内容
for i, child in enumerate(soup.body.div.ul.contents):
    print(i, child)
print('---------------')
# 由于对children迭代时没有使用enumeration函数，所以需要单独定义一个变量i来保存元素的索引
i = 1
# 对ul中的所有子节点进行迭代，并以文本形式输出子节点的内容
for child in soup.body.div.ul.children:
    print('<', i, '>', child, end=' ')
    i += 1
print('----------------')
# 对ul中的所有子孙节点进行迭代，并以文本形式输出子节点的内容
for i, child in enumerate(soup.body.div.ul.descendants):
    print('[', i, ']', child)