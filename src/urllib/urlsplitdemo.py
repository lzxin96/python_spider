from urllib.parse import urlsplit,urlunsplit
# 将URL拆成5部分
result = urlsplit('https://search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment')
print('scheme：',result.scheme)
print('netloc：',result.netloc)
print('path：',result.path) # path=path+param
print('query：',result.query)
print('fragment：',result.fragment)
print('-----------------')

# 拆分URL,指定scheme，并且忽略fragment
result = urlsplit('search.jd.com/Searchprint;hello?keyword=Python从菜鸟到高手&enc=utf-8#comment',scheme='ftp',allow_fragments=False)
print('scheme：',result.scheme)
print('fragment：',result.fragment)
print('----------------')
 # 将5部分合并完整的URL
data = ['https','search.jd.com','Searchprint;world','keyword=Python从菜鸟到高手&enc=utf-8','comment']
print(urlunsplit(data))


