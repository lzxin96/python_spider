from urllib.robotparser import RobotFileParser
from urllib import request

robot = RobotFileParser()
url = 'https://www.jd.com/robots.txt'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Host':'localhost'
}
req = request.Request(url=url, headers=headers)

# 抓取robots.txt文件的内容，并提交个parse方法进行分析
robot.parse(request.urlopen(req).read().decode('utf-8').split('\n'))
# 输出T
print(robot.can_fetch('*', 'https://jd.com'))
# 输出T
# print(robot.can_fetch('*', 'https://www.jianshu.com/p/92f6ac2c350f'))
# 输出F
# print(robot.can_fetch('*', 'https://www.jianshu.com/search?q=Python&page=1&type=note'))