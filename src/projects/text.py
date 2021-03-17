from urllib import request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

# 获取页面
def getPage(url):
    req = request.Request(url, headers=headers, method="GET")
    response = request.urlopen(req)
    result = []
    if response.stats == 200:
        html = response.read().decode('utf=8')
        aList = re.findall('<li>.*</li>', html)
        for a in aList:
            g = re.findall('href="([^">]*)"[\s]*title="([^">])"', a)
            if g != None:
                url = 'http://www.doupoxs.com' + g.group(1)
                title = g.group(2)
                chapter = {'url':url, 'title':title}
                result.append(chapter)
    return result

# 抓取文章内容
def getContent(chapters):
    for chapter in chapters:
        req = request.Request(url=chapter['url'], headers=headers, method="GET")
        response = request.urlopen(req)
        if response.status == 200:
            new_title = re.sub('\?', ' ', chapter['title'])
            f = open('novel/' + new_title + '.txt', 'a+', encoding="UTF-8")
            contents = re.findall('<p>(.*?)</p>', response.read().decode("utf-8"))
            for content in contents:
                f.write(content + '\n')
            f.close()
            print(chapter['title'], chapter['url'])

getContent(getPage('http://www.doupoxs.com/nalanwudi'))