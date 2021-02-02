from urllib import request
import re

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

# 根据小说链接得到小说目录和对应的URL，该函数返回catelogs列表
def getCatelogs(url):
    # 请求小说目录页面
    req = request.Request(url=url, headers=headers, method="GET")
    # 发送请求
    response = request.urlopen(req)
    # 返回数据
    result =[]
    if response.status == 200:
        # 读取界面
        html = response.read().decode('utf-8')
        # 得到<li></li>节点列表
        aList = re.findall('<li>.*</li>', html)
        # 开始获取每一个<li>节点中的href和title属性值，分别得到URL和标题
        for a in aList:
            # 过滤出URL和标题
            # [^...]不匹配[]中的字符
            g = re.search('href="([^>"]*)"[\s]*title="([^>"]*)"', a)
            # 填充url和标题
            if g != None:
                url = 'http://www.doupoxs.com' + g.group(1)
                title = g.group(2)
                # 创建一个对象，用于保存标题和url
                chapter = {'title':title, 'url':url}
                result.append(chapter)
    return result

# 根据章节目录，抓取目录对应的URL指定的小说正文页面
def getCharterContent(chapters):
    for chapter in chapters:
        # 定义Reques对象，用于指定请求头
        req = request.Request(url=chapter['url'], headers=headers, method="GET")
        # 发送请求
        response = request.urlopen(req)
        # 如果状态码是200，则继续往下执行
        if response.status == 200:
            # 去除标题中特殊字符
            new_title = re.sub('\?',' ', chapter['title'])
            # 打开novel目录下的本地文件，以标题命名，扩展名为txt
            f = open('novel/' + new_title + '.txt', 'a+', encoding='utf-8')
            # 将加载<p>节点中的文本提出来
            contents = re.findall('<p>(.*?)</p>', response.read().decode('utf-8'))
            for content in contents:
                # <p>节点中的内容一行行的添加到文件中
                f.write(content + '\n')
            # 关闭文件句柄
            f.close()
            print(chapter['title'], chapter['url'])

# 开始抓取小说目录和正文
getCharterContent(getCatelogs('http://www.doupoxs.com/nalanwudi'))

