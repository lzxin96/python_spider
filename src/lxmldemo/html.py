from lxml import etree

# 创建lxml.etree.HTMLParser对象
parser = etree.HTMLParser()
print(type(parser))
# 读取并解析test.html文件
tree = etree.parse('test.html', parser)
# 获取根节点
root = tree.getroot()

# 将HTML文档转换为可读格式
result = etree.tostring(root, encoding='utf-8', pretty_print=True, method="html")
print(str(result, 'utf-8'))

# 输出根节点的名称
print(root.tag)
# 输出根节点lang属性的值
print('lang = ', root.get('lang'))
# 输出mate界面的charset属性的值
print('charset = ', root[0][0].get('charset'))
# 输出title界面文本
print('text = ', root[0][1].text)