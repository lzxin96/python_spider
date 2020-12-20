from urllib.parse import urlparse,urlunparse

#拆分URL
result = urlparse('https://search.jd.com/Secrchprint;hello?keyword=Python从菜鸟到高手&utf-8#comment')
print('scheme:', result.scheme)
print('netloc:', result.netloc)
print('path:', result.path)
print('params:', result.params)
print('query:', result.query)
print('fragment', result.fragment)
print('---------------------')

# 拆分URL,指定scheme，并且忽略fragment
result = urlparse('search.jd.com/Secrchprint;hello?keyword=Python从菜鸟到高手&utf-8#comment', 
                    scheme='ftp', allow_fragments=False)
print('scheme:', result.scheme)
print('fragment', result.fragment)
print('---------------------')

# 合并不同部分，组成一个完整的URL,必须存入6个元素
data = ['https', 'search.jd.com', 'Searchprint', 'world', 'keyword=Python从菜鸟到高手&utf-8', 'comment']
print(urlunparse(data))