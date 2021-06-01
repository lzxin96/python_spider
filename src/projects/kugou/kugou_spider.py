import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


# 抓取网络红歌榜某一页面的HTMl代码，并提取出感兴趣的信息
def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # 提取名次
    ranks = soup.select('span.pc_temp_num')
    # 提取歌手和歌曲名
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    # 提取歌曲时长
    times = soup.select('span.pc_temp_tips_r > span')
    for rank, title, time1 in zip(ranks, titles, times):
        data = {
            'rank': rank.get_text().strip(),
            'title': title.get_text().split('-')[0],
            'song': title.get_text().split('-')[1],
            'time': time1.get_text().strip()
        }
        print(data)


if __name__ == '__main__':
    # 产生网络红歌榜前10页的数据
    urls = ['https://www.kugou.com/yy/rank/home/{}-23784.html?from=rank'.format(str(i)) for i in range(1, 3)]
    # 处理网络红歌榜前10页的数据
    for url in urls:
        get_info(url)
        time.sleep(2)
