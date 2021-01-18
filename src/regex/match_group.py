import re

# match第一个参数指定文本模式，第二个参数表示待匹配的字符串
m = re.match('hello','hello')
if m is not None:
    # 匹配成功，输出hello，返回match对象
    print(m.group())
# 输出m的类名，SER_Match
print(m.__class__.__name__)

m = re.match('hello', 'world')
if m is not None:
    # 匹配失败，m=None
    print(m.group())
print(m)

m = re.match('hello', 'hello world')
if m is not None:
    # 只要模式从字符串起始位置开始，也可以匹配成功
    print(m.group())
print(m)