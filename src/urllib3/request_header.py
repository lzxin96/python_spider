from urllib3 import *
import re

disable_warnings()
http = PoolManager()

# 定义天猫的搜索页面URL
url = r"https://list.tmall.com/search_product.htm?q=%CA%FE%BF%DA%CB%AE&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton"
# 从headers.txt文件读取HTTP请求头，并将其转换为字典形式
def str2Headers(file):
    headerDict = {}#字典
    f = open(file, 'r')# r:只读；rb：二进制读
    # 读取headers.txt文件中的所有内容
    headerText = f.read()
    # 以回车为断点，分割字段
    headers = re.split('\n', headerText)
    for header in headers:
        result = re.split(':', header, maxsplit=1)# maxsplit表示最大分割次数
        headerDict[result[0]] = result[1]
    f.close()# 关闭文件
    return headerDict

headers = str2Headers('D:/py_space/spider/python_spider/src/urllib3/headers.txt')
# 请求天猫的搜索也面，并传递HTTP请求头
response = http.request('GET', url, headers=headers)
# 将服务端返回的数据按GB18030格式解码
data = response.data.decode('GB18030')
print(data)