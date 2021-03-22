from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('D:/py_space/spider/python_spider/src/xpath/demo.html', parser)

# 选取demo.html文件中所有的节点
nodes = html.xpath('//*')
print('共', len(nodes), '个节点')
print(nodes)

# 输出所有节点的节点名
for i in range(0, len(nodes)):
    print(nodes[i].tag, end=' ')

# 按层次输出节点，indent是缩进
def printNodeTree(node, indent):
    print(indent + node.tag)
    indent += "  "
    children = node.getchildren()
    if len(children) > 0:
        for i in range(0, len(children)):
            # 递归调用
            printNodeTree(children[i], indent)
print()
# 按层次输出节点的节点，nodes[0]是根节点(html节点)
printNodeTree(nodes[0], "")

# 选取demo.html文件中所有的<a>节点
nodes = html.xpath('//a')
print()
print('共', len(nodes), '个<a>节点')
print(nodes)
# 输出所有<a>节点的文本
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')