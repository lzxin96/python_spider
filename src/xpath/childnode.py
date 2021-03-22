from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)

# 成功选取<a>节点
nodes = html.xpath('//li/a')
print('共 ', len(nodes), '个节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')

print()
# 成功选取<a>节点
nodes = html.xpath('//ul//a')
print('共 ', len(nodes), '个节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')

print()
# 无法选取<a>节点，因为<a>不是<ul>的直接子节点
nodes = html.xpath('//ul/a')
print('共 ', len(nodes), '个节点')
print(nodes)