from bs4 import BeautifulSoup
html = '''
<div>
    <ul>
        <li class="item1" value1="1234" value2 = "hello world"><a href="https://geekori.com"> geekori.com</a></li>
        <li class="item">
           <a href="https://www.jd.com"> 京东商城</a>
           <a href="https://www.google.com">谷歌</a>
        </li>        
    </ul>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">淘宝</a></li>
        <li class="item" ><a href="https://www.microsoft.com">微软</a></li>
    </ul>
</div>

'''

soup = BeautifulSoup(html,'lxml')
# 选取class属性值为item的所有节点
tags = soup.select('.item')
# select方法返回列表类型，列表元素类型是Tag对象
print(type(tags))
for tag in tags:
    # 在当前节点中选取节点名为a的所有节点
    aTags = tag.select('a')
    for aTag in aTags:
        print(aTag)

print('---------')
for tag in tags:
    # 通过方法选择器选取节点名为a的所有节点
    aTags = tag.find_all(name='a')
    for aTag in aTags:
        print(aTag)