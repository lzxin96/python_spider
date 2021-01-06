import requests
# 抓取图像文件，其中http://t.cn/EfgN7gz是图像文件的短链接
r = requests.get('https://pics3.baidu.com/feed/c995d143ad4bd113d913527dc3047e0849fb05d2.jpeg?token=ce60f7ca1456f20d4eafbd67837ebe3f&s=66F1398D2ACB66DCF6092DDE03008033')
# 输出文件的内容，不过是乱码
print(r.text)

# 将图像保存为本地文件
# 保存二进制文件，需要保存在本地
# content抓取图片、pdf文档不会变乱码
with open('Python从菜鸟到高手.png','wb') as f:
    f.write(r.content)