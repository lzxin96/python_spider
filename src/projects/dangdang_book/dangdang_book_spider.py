from pyquery import PyQuery as pq
import requests
import time


# 爬取当当网相关图书：图书主页URL、图示标题（图书名）、图书当前价格、图书作者、出版日期、出版社、评论数、简介
# http://search.dangdang.com/?key=python&act=input
# 用于下载指定URL的页面
def get_one_page(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        return None
    except Exception:
        return None

# 分析搜索也是一个产生器函数
def parse_one_page(html):
    pass