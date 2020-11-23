from flask import Flask
from flask import request

app = Flask(__name__)
# 输出客户端发送过来的所有的Cookie，以及名为Cookie的Cookie的值
@app.route("/readCookie")
def readCookie():
    print(request.cookies)
    print(request.cookies.get('MyCookie'))
    return 'hello world'

# 向客户端写入名为id的cookie（设置Set-Cookie字段）
@app.route("/writeCookie")
def writeCookie():
    response = app.make_response('write cookie')
    # 写入Cookie
    response.set_cookie("id", value="12345678")
    return response

if __name__ == '__main__':
    app.run()