from urllib.parse import urljoin

# urljoin(base_url, url)
# base_url:基URL，只能设置scheme、netloc、path
# url：不是一个完整的URL，会将第2个参数的值加到第1个参数后面，自动补齐（/）；如果第2个参数为完整的URL，则直接返回第2个参数的值

# 输出https://www.jd.com/index.html
print(urljoin('https://www.jd.com','index.html'))
# 输出https://www.taobao.com
print(urljoin('https://www.jd.com','https://www.taobao.com'))
# 输出https://www.taobao.com/index.html
print(urljoin('https://www.jd.com/index.html','https://www.taobao.com/index.html'))
# 输出https://www.jd.com/index.php?name=Bill&age=30
print(urljoin('https://www.jd.com/index.php','?name=Bill&age=30'))
# 输出https://www.jd.com/index.php?name=Bill
print(urljoin('https://www.jd.com/index.php?value=123','?name=Bill'))