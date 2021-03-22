from lxml import etree

# 创建lxml.etree.HTMLParser对象
parser = etree.HTMLParser()
tree = etree.parse('test.html', parser)
# 使用XPath定位title节点，返回一个节点集合
titles = tree.xpath('/html/head/title')
if len(titles) > 0:
    # 输出title节点的文本
    print(titles[0].text)
# 定义一段HTML代码
html = '''
<div>
    <ul>
        <li class="item1"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com"> 京东商城</a></li>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
    </ul>
</div>
'''
# 分析HTML代码
tree = etree.HTML(html)
# 使用XPath定位class属性值为item2的<li>节点
aTags = tree.xpath("//li[@class='item2']")
if len(aTags) > 0:
    # 得到该<li>节点中<a>节点的href属性值和文本
    print(aTags[0][0].get('href'), aTags[0][0].text)