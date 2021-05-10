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
        <li class="item1" value1="1234" value2 = "hello world">
            <a href="https://geekori.com"> geekori.com</a>
        </li>
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
# 得到第2个节点，soup.li.next_sibling指的是文本节点（包含\n字符）
secondli = soup.li.next_sibling.next_sibling
# 输出低2个li节点的代码
print('第1个li节点的下一个li节点：',secondli)
# 获得第2个li节点的上一个同级的li节点，并输出该li节点的class属性的值
print('第2个li节点的上一个li节点的class属性值：', secondli.previous_sibling.previous_sibling['class'])
# 输出第2个li节点后的所有节点，包括带换行符的文本节点
for sibling in secondli.next_siblings:
    print(type(sibling))
    # strip去除两端空格
    if str.strip(sibling.string) == '':
        print('换行')
    else:
        print(sibling)