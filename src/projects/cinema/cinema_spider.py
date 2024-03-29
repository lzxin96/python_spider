import json
from urllib3 import *
import re
import time

disable_warnings()
# 创建连接池
http = PoolManager()

# 得到单个页面的HTML代码
# Cookie+https请求可以绕过验证中心
def getOnePage(url):
    try:
        headers ={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
            'Cookie': '__mta=216389545.1612194708063.1616830838685.1616830986889.9; _lxsdk_cuid=1775db0be51c8-02f190926dc331-c791e37-144000-1775db0be52c8; uuid_n_v=v1; uuid=07E649908ECB11EB9B517940D4CC68F5FA7CFE3C7E274C828776399A9C818338; _lxsdk=07E649908ECB11EB9B517940D4CC68F5FA7CFE3C7E274C828776399A9C818338; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1616828824,1616829906; _csrf=07da9d0e23217f72bb67d3fcaee29b1cf30325c67dffb6f9790fd0b00928f0d8; __mta=42947098.1612184600180.1616830265531.1616830363889.18; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1616831465; _lxsdk_s=1787281faa4-67b-e56-791%7C%7C56'
        }
        # 发送请求（包含请求头）
        response = http.request('GET', url, headers=headers)
        # 获取HTML代码
        data = response.data.decode('utf-8')
        # 如果成功响应，返回HTML代码
        if response.status == 200:
            return data
        return None
    except Exception:
        return None

# 分析页面，这是一个生成器（Generator）函数，可以对返回值迭代
def parseOnePage(html):
    # 使用正则表达式分析HTML代码
    # re.S是指"."的作用扩展到整个字符串，包括\n，"."默认只针对一行有效
    '''
    预编译：compile()
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：
    1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    2.用编译后的正则表达式去匹配字符串。
    '''
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # 得到页面中所有匹配的项
    items = re.findall(pattern, html)
    for item in items:
        # 将函数变成一个Generator，可以进行迭代
        yield {
            # 得到电影索引、图像URL、电影图标、演员列表、上映时间、评分
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

# 保存抓取的数据
def save(content):
    with open('board.txt', 'a', encoding='utf-8') as f:
        # 将JSON对象转换为字符串，ensure_ascii为False，表示返回的值可以包括非ASCII字符
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

# 根据偏移量，抓取并保存每一页的电影数据
def getBoard(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = getOnePage(url)
    # 使用产生器函数进行迭代，处理每一页的每一部电影数据
    for item in parseOnePage(html):
        print(item)
        save(item)

# 处理10页电影榜单
for i in range(10):
    getBoard(offset=i * 10)
    time.sleep(3)

