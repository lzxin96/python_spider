from bs4 import BeautifulSoup
import requests
import time
import json

headers = {
    'User-Agent': '...'
}
# 将房源实景图保存到本地
def save_house_image(url, name):
    r = requests.get(url)
    name = str.replace(name, '/', '')
    with open('images/' + name, 'wb') as f:
        f.write(r.content)

# 抓取小猪网沈阳地区房源首页的HTML代码，并得到本页所有房源的URL
def get_links(url):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, 'lxml')
    # 提取包含所有<a>标签的<div>标签
    links = soup.find_all(class_='resule_img_a')
    # 进行迭代，并通过get_info函数处理每个房源的页面
    for link in links:
        href = link['href']
        house_info = get_info(href)
        print(house_info)
        # 将房源信息已JSON格式保存到house.txt中
        f.write(json.dumps(house_info, ensure_ascii=False) + '\n')

# 从房源主页的HTML代码中提取标题、地址、价格等信息，并以字段形式返回这些信息
def get_info(url):
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result, 'lxml')
    div = soup.find(class_ = 'php_info')
    # 提取标题
    title = div.h4.em.string
    # 提取地址
    address = div.p.span.string
    # 提取价格
    price = soup.find(class_ = 'detail_avgprice').string
    # 提取图像的URL
    image_url = soup.find(id = 'curBigImage')['src']
    # 提取房主昵称
    name = soup.find(class_ = 'lorder_name').string
    # 提取与性别相关的信息
    member_ico = soup.find(class_ = 'member_boy_ico')
    sex = '男'
    if member_ico == None:
        sex = '女'
    info = {
        'title':title,
        'address':address.strip(),
        'price':price,
        'image_url':image_url,
        'name':name,
        'sex':sex
    }
    # 保存图像
    save_house_image(image_url, title + ".png")
    return info

if __name__ == '__main__':
    f = open('./houses.txt', 'a+')
    # 生成前10页房源页面的URL
    urls = ['http://sy.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,11)]
    # 开始住区和分析前10页房源页面的HTML代码
    for single_url in urls:
        get_links(single_url)
        time.sleep(1)
    f.close()