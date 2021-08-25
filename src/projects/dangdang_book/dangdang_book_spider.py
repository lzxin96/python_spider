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
    doc = pq(html)
    # 提取包含所有li节点的ul节点
    ul = doc('.bigimg')
    liList = ul('li')
    # 对li节点集合进行迭代，这里要注意，必须使用items方法返回可迭代的对象，这样每一个item才会是PyQuery对象
    for li in liList.items():
        # 获取当前li节点中第1个a节点
        a = li('a:first-child')
        # 获取图书主页的URL
        href = a[0].get('href')
        # 获取图书名称
        title = a.attr('title')
        # 抓取class属性值为search_now_price的节点
        span = li('.search_now_price')
        # 获取价格
        price = span[0].text[1:]
        # 抓取class属性值为search_book_author的节点
        p = li('.search_book_author')
        # 获取图书作者
        author = p('a:first-child').attr('title')
        # 获取图书出版日期
        date = p('span:nth-child(2)').text()[1:]
        # 获取图书出版社
        pubilsher = p('span:nth-child(3)').text()
        # 获取图书评论数
        comment_number = li('.search_comment_num').text()[:-3]
        # 获取图书简介
        detail = li('.detail').text()
        yield {
            'herf': href,
            'title': title,
            'price': price,
            'author': author,
            'date': date,
            'pubilsher': pubilsher,
            'comment_number': comment_number,
            'detail': detail
        }


if __name__ == '__main__':
    # 产生前x页的URL
    urls = ['http://search.dangdang.com/?key=python&act=input&sort_type=sort_default&page_index={}'.format(str(i)) for i in range(1, 2)]
    # 处理这x个url对应的3个搜索页面
    for url in urls:
        book_infos = parse_one_page(get_one_page(url))
        for book_info in book_infos:
            # 输出每一本图书的信息
            print(book_info)
            time.sleep(1)