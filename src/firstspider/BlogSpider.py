from urllib3 import *
from re import *

http = PoolManager()
# 禁止显示警告信息
disable_warnings()

# 下载url对应的web页面
def download(url):
    result = http.request('GET', url)
    # 获取web页面对应的html代码
    htmlStr = result.data.decode('utf-8')
    return htmlStr

# 分析HTML代码
def analyse(htmlStr):
    # 通过正则表达式获取所有class属性值为post-item-title的<a>节点
    aList = findall('<a[^>]*post-item-title[^>]*>[^<]*</a>',htmlStr)
    result = []
    # 提取每一个<a>节点中的url
    for a in aList:
        # 利用正则表达式提取<a>节点中的url
        g = search('href[\s]*=[\s]*[\'"]([^>\'""]*)[\'"]', a)
        if g != None:
            url = g.group(1)# 得到url
        # 通过查找的方式提取<a>节点中的博客的标题
        index1 = a.find(">")
        index2 = a.rfind("<")
        # 获取博客标题(切片)
        title = a[index1 + 1 : index2]
        # 创建字典
        d = {}
        d['url'] = url
        d['title'] = title
        result.append(d)
    # 返回一个包含博客标题和url的对象
    return result

# 抓取博客列表
def crawler(url):
    html = download(url)
    blogList = analyse(html)
    for blog in blogList:
        print("title:",blog["title"])
        print("url:",blog["url"])


crawler('https://www.cnblogs.com')