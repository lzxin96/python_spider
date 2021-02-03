import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
}

jokeLists = []
# 判断性别
def verifySex(class_name):
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'

def getJoke(url):
    # 获取页面的HTML代码
    res = requests.get(url)
    # 获取用户ID
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    # 获取用户级别
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    # 获取性别
    sexs = re.findall('<div class="articleGender (.*?)">',res.text, re.S)
    # 获取段子内容
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text, re.S)
    # 获取好笑数
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text, re.S)
    # 获取评论数
    comments = re.findall('<i class="number">(\d+)</i> 评论',res.text, re.S)
    '''
    使用zip函数将上述获得的数据的对应索引的元素放到一起
    zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    如将[1,2]、['a','b']变成[(1,'a'),(2,'b')]形式，以便对每一个元素进行迭代
    '''
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        # 获得每个段子相关的数据
        info = {
            'id':id,
            'level':level,
            'sex':verifySex(sex),
            'content':content,
            'laugh':laugh,
            'comment':comment
        }
        jokeLists.append(info)

# 产生1~30页的URL
urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,31)]
# 对着30个URL进行迭代，获取这30页的段子
for url in urls:
    getJoke(url)

# 将抓取结果保存在当前目录jokes.txt文件中
for joke in jokeLists:
    f = open('./jokes.txt', 'a+', encoding='utf-8')
    try:
        f.write(joke['id']+'\n')
        f.write(joke['level'] + '\n')
        f.write(joke['sex'] + '\n')
        f.write(joke['content'] + '\n')
        f.write(joke['laugh'] + '\n')
        f.write(joke['comment'] + '\n\n')
        f.close()
    except UnicodeEncodeError:
        pass