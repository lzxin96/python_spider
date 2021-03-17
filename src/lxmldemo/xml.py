from lxml import etree

# 读取products.xml文件
tree = etree.parse('products.xml')
print(type(tree))

# 将tree重新转换为字符串形式的xml文档，并输出
print(str(etree.tostring(tree, encoding='utf-8'), 'utf-8'))

# 获取根节点对象
root = tree.getroot()
print(type(root))

# 输出根节点的名称
print('root:', root.tag)
# 获取根节点的所有子节点
children = root.getchildren()
print('---------------输出产品信息-----------------')

# 迭代这些子节点，并输出对应的属性和节点文本
for child in children:
    print('product id = ', child.get('id'))
    print('child[0].name = ', child[0].text)
    print('child[1].price = ', child[1].text)

# 分析字符串形式的xml文档
root = etree.fromstring('''
<products>
    <product name="iphone"/>
    <product name="ipad"/>
</products>
''')
print('--------------新产品------------------')
# 输出根节点节点名
print('root =', root.tag)
children = root.getchildren()
# 迭代这些子节点，并输出节点的名称和name属性
for child in children:
    print(child.tag, 'name = ', child.get('name'))