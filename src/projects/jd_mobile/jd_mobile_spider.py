from pyquery import PyQuery as pq
import requests
import time
import xlwt

# 根据搜索页面URL抓取对应的HTML代码
def get_one_page(url):
    try:
        # 请求头，在京东商城搜索必须处于登录状态，所以需要发送cookie
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        }
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            # 如果直接使用result.text获取文本，中文会出现乱码
            # 先获取二进制形式的响应内容
            html = result.content
            # 将二进制响应内容按utf-8格式转化为文本内容
            html_doc = str(html, 'utf-8')
            return html_doc
        return None
    except Exception:
        return None

# 分析搜索页面的HTML代码，该函数是一个产生器函数
def parse_one_page(html):
    doc = pq(html)
    # 获取ul节点
    ul = doc('.gl-warp.clearfix')
    # 获取该ul节点中的所有li节点
    liList = ul('.gl-item')
    # 处理每个li节点，这里必须使用items函数获得每个li节点，这样才能获得PyQuery对象
    for li in liList.items():
        # 获取手机产品名称
        product = li(' div > div.p-name.p-name-type-2 > a > em').text()
        # 如果None，说明是京东精选，要使用另一个CSS选择器
        # if product is None:
        #     product = li(' div > div.p-name.p-name-type-2 > a').attr('title')
        # 获取产品价格
        price = li(' div > div.p-price > strong > i').text()
        # 获取产品卖家
        seller = li(' div > div.p-shop > span > a').text()
        yield {
            'product': product,
            'price': price,
            'seller': seller
        }
    
if __name__ == '__main__':
    # 产生前4页的URL
    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&psort=3&suggest=1.his.0.0&wq=%E6%89%8B%E6%9C%BA&psort=3&pvid=59640d40d4ed4de9ba3c3c531ca4f115&page={}&s=61&click=0'.format(str(i)) for i in range(1, 3, 5)]
    # 定义Excel文件的头
    header = ['排名', '产品', '价格', '卖家']
    book = xlwt.Workbook(encoding='utf-8')
    # 为所有手机排行创建Sheet
    sheet_all = book.add_sheet('所有手机销量排名')
    # 为Apple手机排行创建Sheet
    sheet_apple = book.add_sheet('apple手机销量排名')
    # 为华为手机排行创建Sheet
    sheet_huawei = book.add_sheet('huawei手机销量排名')
    # 为小米手机排行创建Sheet
    sheet_xiaomi = book.add_sheet('小米手机销量排名')
    # 为每一个Sheet添加表头
    for h in range(len(header)):
        sheet_all.write(0, h, header[h])
        sheet_apple.write(0, h, header[h])
        sheet_huawei.write(0, h, header[h])
        sheet_xiaomi.write(0, h, header[h])
    # 下面4个变量分别控制总排行的名称，Apple、华为、小米手机排行的名称
    i = 1
    apple_i = 1
    huawei_i = 1
    xiaomi_i = 1
    for url in urls:
        mobile_infos = parse_one_page(get_one_page(url))
        # 处理每一步手机的信息
        for mobile_info in mobile_infos:
            print(mobile_info)
            # 将手机信息添加到第1个Sheet中
            sheet_all.write(i, 0, str(i))
            sheet_all.write(i, 1, mobile_info['product'])
            sheet_all.write(i, 2, mobile_info['price'])
            sheet_all.write(i, 3, mobile_info['seller'])
            # 在产品名称中搜索，如果包含apple，说明是Apple手机，将该手机信息添加到第2个Sheet中
            if mobile_info['product'].lower().find('apple') != -1:
                sheet_apple.write(apple_i, 0, str(apple_i))
                sheet_apple.write(apple_i, 1, mobile_info['product'])
                sheet_apple.write(apple_i, 2, mobile_info['price'])
                sheet_apple.write(apple_i, 3, mobile_info['seller'])
                apple_i += 1
            # 在产品名称中搜索，如果包含华为，说明是华为手机，将该手机信息添加到第3个Sheet中
            if mobile_info['product'].lower().find('华为') != -1:
                sheet_huawei.write(huawei_i, 0, str(huawei_i))
                sheet_huawei.write(huawei_i, 1, mobile_info['product'])
                sheet_huawei.write(huawei_i, 2, mobile_info['price'])
                sheet_huawei.write(huawei_i, 3, mobile_info['seller'])
                huawei_i += 1
            # 在产品名称中搜索，如果包含小米，说明是小米手机，将该手机信息添加到第4个Sheet中
            if mobile_info['product'].lower().find('小米') != -1:
                sheet_xiaomi.write(xiaomi_i, 0, str(xiaomi_i))
                sheet_xiaomi.write(xiaomi_i, 1, mobile_info['product'])
                sheet_xiaomi.write(xiaomi_i, 2, mobile_info['price'])
                sheet_xiaomi.write(xiaomi_i, 3, mobile_info['seller'])
                xiaomi_i += 1
            time.sleep(0.1)
            i += 1
    # 生成包含手机排行数据的Excel文件
    book.save(r'D:\py_space\spider\python_spider\src\projects\jd_mobile\mobile_rank.xls')