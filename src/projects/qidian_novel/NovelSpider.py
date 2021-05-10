import requests
from lxml import etree
import xlwt
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}
# 根据指定页面的URL获取单圈页面所有小说的相关信息，该函数是一个产生器函数
def getOnePage(url):
    # 抓取小说页面代码
    res = requests.get(url, headers=headers)
    # 获取所有节点
    selector = etree.HTML(res.text)
    # 选择<ul>节点中所有的<li>节点
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for info in infos:
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        yield {
            # 提取标题
            'title': info.xpath('div[2]/h4/a/text()')[0],
            # 提取作者
            'author': info.xpath('div[2]/p[1]/a[1]/text()')[0],
            # 提取风格
            'style': style_1 + '~' + style_2,
            # 提取完成度
            'complete': info.xpath('div[2]/p[1]/span/text()')[0],
            # 提取介绍
            'introduce': info.xpath('div[2]/p[2]/text()')[0].strip()
        }

# 制作Excel表格，定义表头
header = ['标题', '作者', '类型', '完成度', '介绍']
# 创建Workbook对象
book = xlwt.Workbook(encoding='utf-8')
# 添加一个名为novels的Sheet
sheet = book.add_sheet('novels')
# 为Excel表单添加表头
for h in range(len(header)):
    sheet.write(0, h, header[h])

# 产生前5页的URL
urls = ['https://www.qidian.com/all/?page={}'.format(str(i)) for i in range(1, 6)]
i = 1
# 开始抓取页面中的小说数据，并将提取的数据保存到Excel的sheet中
for url in urls:
    novels = getOnePage(url)
    for novel in novels:
        print(novel)
        time.sleep(0.1)
        sheet.write(i, 0, novel['title'])
        sheet.write(i, 1, novel['author'])
        sheet.write(i, 2, novel['style'])
        sheet.write(i, 3, novel['complete'])
        sheet.write(i, 4, novel['introduce'])
        i += 1
# 将内存中的Excel数据保存为novels.xls文件
book.save('novels.xls')