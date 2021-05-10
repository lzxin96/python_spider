from lxml import *
from lxml import etree
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

# 根据url抓取HTML代码，并返回这些代码，如果抓取失败，返回空
def getOnePage(url):
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None

# 分析HTML代码，这是一个产生器函数
def parseOnePage(html):
    selector = etree.HTML(html)
    # 选择<tr>节点
    items = selector.xpath('//tr[@class="item"]')
    # 在<tr>节点中继续使用XPath选择对应节点
    for item in items:
        # 获取<p>节点中的文本，其中包含出版社、作者、出版日期等信息
        book_infos = item.xpath('td/p/text()')[0]
        yield {
            # 获取图书名称
            'name': item.xpath('td/div/a/@title')[0],
            # 获取图书主页链接
            'url': item.xpath('td/div/a/@href')[0],
            # 获取图书作者
            'author': book_infos.split('/')[0],
            # 获取图书出版社
            'publisher': book_infos.split('/')[-3],
            # 获取出版日期
            'date': book_infos.split('/')[-2],
            # 获取图书价格
            'price': book_infos.split('/')[-1]
        }

# 将抓取到的数据（JSON格式）保存到top250books.txt文件中
def save(content):
    with open('top250books.txt', 'a+', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 抓取url对应的界面，并将页面内容保存到top250books.txt文件中
def getTop250(url):
    html = getOnePage(url)
    for item in parseOnePage(html):
        print(item)
        save(item)

# 产生10个URL，分别对应Top250排行榜的10个页面的URL
urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
# 循环抓取Top250排行榜的10个页面的图书信息
for url in urls:
    getTop250(url)
# getTop250('https://book.douban.com/top250?start=0')