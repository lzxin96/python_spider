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
        <li class="item1"><a href="https://www.jd.com"> 京东商城</a></li>        
    </ul>
</div>
</body>
</html>
'''

soup = BeautifulSoup(html,'lxml')
# 选取head节点
print(soup.head)
# 输出head节点的内容
print(type(soup.head))
# 将head节点对应的Tag对象赋给head变量
head = soup.head
# 在head节点的基础上继续嵌套选择title节点，并输出title节点的文本信息
print(head.title.string)
# 嵌套选择a节点，并输出a节点的href属性的值
print(soup.body.div.ul.li.a['href'])



