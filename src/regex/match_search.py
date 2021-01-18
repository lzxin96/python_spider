import re

# 进行文本模式匹配，匹配失败，match方法返回None
m = re.match('python', 'I love python.')
if m is not None:
    print(m.group())
print(m)

# 进行文本模式搜索，搜索成功
m = re.search('python', 'I love python.')
if m is not None:
    # 运行结果：python
    print(m.group())
print(m)