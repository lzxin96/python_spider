from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)

# 选取href属性值为https://www.jd.com或https://geekori.com的<a>节点
aList = html.xpath('//a[@href="https://www.jd.com" or @href="https://geekori.com"]')
for a in aList:
    print(a.text, a.get('href'))

# 匹配<li class="item4" value="1234"><a href="https://www.microsoft.com">微软</a></li>
# 选取href属性值包含www，并且父节点中value属性值等于1234的<a>节点
print('----------------------')
aList = html.xpath('//a[contains(@href,"www") and ../@value="1234"]')
for a in aList:
    print(a.text, a.get('href'))