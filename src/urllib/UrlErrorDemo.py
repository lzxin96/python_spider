from urllib import request,error

try:
    response =  request.urlopen("http://www.jd123.com/test.html")
except error.URLError as e:
    # Bad Request
    print(e.reason)

try:
    response = request.urlopen("https://geekori.com/abc.html")
except error.URLError as e:
    # Not Found
    print(e.reason)

try:
    response = request.urlopen("https://geekori123.com/abc.html")
except error.URLError as e:
    # [Error 8] nodename nor servname provided, or not known
    print(e.reason)

try:
    response = request.urlopen("https://baidu.com", timeout=0.0001)
except error.URLError as e:
    # Time out
    print(e.reason)