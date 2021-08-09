from pyquery import PyQuery as pq


# 分析test.html
doc = pq(filename='D:/py_space/spider/python_spider/src/pyquery/test.html')
# 获取class属性值的item的所有节点
result = doc('.item')
# 查找这些节点之直接父节点
print(result.parent())
print('------------')
print('父节点数：', len(result.parents()))
# 查找这些节点的所有父节点
print(result.parents())
# 查找id属性值为panel的父节点
print('父节点数：', len(result.parents('#panel')), '节点名：', result.parents('#panel')[0].tag)