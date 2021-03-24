import requests
from lxml import etree

# 抓取京东商城首页的HTML代码
r = requests.get('http://www.jd.com')
parser = etree.HTMLParser()
html = etree.HTML(r.text)
# 提取导航条第1部分链接文本
nodes = html.xpath('//*[@id="navitems-group1"]//a/@aria-lable')
print(nodes)
# 提取导航条第2部分链接文本
nodes = html.xpath('//*[@id="navitems-group2"]//a/text()')
print(nodes)
# 提取导航条第3部分链接文本
nodes = html.xpath('//*[@id="navitems-group3"]//a/text()')
print(nodes)