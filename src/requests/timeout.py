import requests,requests.exceptions

try:
    # 会抛出超时异常,连接和读取时间不能超过0.01秒
    r = requests.get('https://www.jd.com', timeout=0.01)
    print(r.text)
except requests.exceptions.Timeout as e:
    print(e)

# 抛出连接超时异常
requests.get('https://www.jd.com', timeout=(0.001,0.01))

# 永久等待，不会抛出异常超时
requests.get('https://www.jd.com', timeout=None)