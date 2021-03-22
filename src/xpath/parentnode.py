from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)

# 选取href属性值为https://www.jd.com的<a>节点的父节点，并输出父节点的class属性值
result = html.xpath('//a[@href="https://www.jd.com"]/../@class')
print('class属性值 =', result)
# 选取href属性值为https://www.jd.com的<a>节点的父节点，并输出父节点的class属性值
result = html.xpath('//a[@href="https://www.jd.com"]/parent::*/@class')
print('class属性值 =', result)