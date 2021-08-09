from pyquery import PyQuery as pq

doc = pq(filename='D:/py_space/spider/python_spider/src/pyquery/test.html')
result = doc('.item')
# 查找class属性值为item的节点的所有兄弟节点
print(result.siblings())
print('----------------')
# 查找class属性值为item2的兄弟节点
print(result.siblings('.item2'))