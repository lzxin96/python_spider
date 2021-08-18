from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1" >
        <li class="item1 item2 item3" >谷歌</li>
        <li class="item1 item2">微软</li>
    </ul>

</div>
'''

doc = pq(html)
# 查询class属性值为item1 item2的节点
li = doc('.item1.item2')
print(li)
# 为查询结果的所有节点添加一个名为myitem的样式
li.addClass('myitem')
print(li)
# 移除查询结果中所有节点的名为item1的样式
li.removeClass('item1')
print(li)
# 移除查询结果中所有节点的两个样式item2 item3
li.removeClass('item2 item3')
print(li)
# 为查询结果的所有节点添加两个样式class1 class2
li.addClass('class1 class2')
print(li)
