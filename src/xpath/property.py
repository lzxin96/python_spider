from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)

# 选取所有href属性值为https://geekori.com的<a>节点
nodes = html.xpath('//a[@href="https://geekori.com"]')
print('共 ', len(nodes), '个节点')
for i in range(0, len(nodes)):
    print(nodes[i].text)

# 选取所有href属性值包含www的<a>节点
nodes = html.xpath('//a[contains(@href,"www")]')
print('共 ', len(nodes), '个节点')
for i in range(0, len(nodes)):
    print(nodes[i].text)

# 获取所有href属性值包含www的<a>节点的href属性值，urls是href属性值的列表
urls = html.xpath('//a[contains(@href,"www")]/@href')
for i in range(0, len(urls)):
    print(urls[i])