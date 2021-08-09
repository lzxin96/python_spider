# coding = utf-8
from pyquery import PyQuery as pq
from lxml import etree

# 分析test.html文件
doc = pq(filename='D:/py_space/spider/python_spider/src/pyquery/test.html')
# 查找所有class属性值为list1的节点，只有第1个ul节点满足条件
result = doc('.list1')
# 查找所有的a的节点，包括子孙节点
aList = result.find('a')
print(type(aList))
for a in aList:
    # 输出每一个查找到的a节点
    print(str(etree.tostring(a, pretty_print=True, encoding='UTF-8'), 'UTF-8'))
print('--------------------')

# 查找所有class属性值为item的所有节点，只有第2个li节点和倒数第2个li节点满足条件
# children之查找直接子节点
result = doc('.item')
aList = result.children('a')
for a in aList:
    # 输出每一个查找到的a节点
    print(str(etree.tostring(a, pretty_print=True, encoding='UTF-8'), 'UTF-8'))