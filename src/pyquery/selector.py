# PyQuery CSS选择器
from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com"> 京东商城</a></li>      
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
        <li class="item2"><a href="https://www.google.com">谷歌</a></li>
    </ul>
</div>
'''
# 创建PyQued对象
doc = pq(html)
# 提取id属性值为panel，并且在该节点中所有class属性值为list1的所有节点
result = doc('#panel .list1')
# 输出result的类型，仍然是PyQuery对象
print(type(result))
print(result)
# 在以result为根的基础上，提取其中class属性值为item的所有节点（本例是li节点）
print(result('.item'))
# 提取其中的第2个a节点的href属性值和文本内容
print(result('a')[1].get('href'), result('a')[1].text)
print()

# 抓取京东商城导航条链接文本
import requests
# 请求京东商城首页，并将返回的HTMl代码传入pq对象
doc = pq(requests.get('https://www.jd.com').text)
# 提取第1个ul节点
group1 = doc('#navitems-group1')
# 输出前4个链接的文本
print(group1('a')[0].text.strip(), group1('a')[1].text.strip(), group1('a')[2].text.strip(), group1('a')[3].text.strip())
# 输出中间4个链接的文本
group2 = doc('#navitems-group2')
print(group2('a')[0].text.strip(), group2('a')[1].text.strip(), group2('a')[2].text.strip(), group2('a')[3].text.strip())
# 输出最后两个链接的文本
group3 = doc('#navitems-group3')
print(group3('a')[0].text.strip(), group3('a')[1].text.strip())