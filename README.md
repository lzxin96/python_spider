# python_spider
爬虫练习代码文件
#### 第一个爬虫实例
* 爬取HTML文件中url：src/firstspider/MySpider.py
* 爬取博客园标题和url：src/firstspider/BlogSpider.py
---------------------------
### 网络库
#### urllib网络库实例
1. urlopen函数发送http get请求：src/urllib/SendRequest.py
2. urlopen函数发送http post请求：src/urllib/PostRequest.py
3. 服务器请求超时异常处理（try...except)：src/urllib/TimeOut.py
4. 设置http请求头(无）：src/urllib/SetRequestHeaders.py
5. 设置中文http请求头：src/urllib/SetChineseRequestHeaders.py
6. 请求基础验证页面：
    src/urllib/AuthService.py（支持基础验证的web服务器）
    src/urllib/Authorization.py（设置Authorization）
    src/urllib/BasicAuth.py(封装请求字段数据)
7. 代理ip设置：src/urllib/HandlerDemo.py
8. 读取和设置Cookie：
    src/urllib/CookieServer.py(设置Cookie服务器)
    src/urllib/CookieBasic.py(获取cookie)
9. 保存cookie为Mozilla格式和LWP格式：src/urllib/CookieFile.py
10. 向服务器发送本地cookie文件：src/urllib/LoadCookie.py
11. robot协议：src/urllib/robotsdemo.py
#### urllib3网络库实例
1. HTTP GET请求
2. HTTP POST请求
3. HTTP请求头 headers关键之
4. HTTP响应头 response.info(),获取响应头字段信息
5. 上传文件
6. 连接超时、读超时
#### requests网络库库实例
1. GET
2. 添加HTTP请求头
3. 抓取二进制数据
4. POST
5. 响应数据Response对象
6. 上传文件
7. 处理Cookie
8. 使用同一个会话Session
9. SSL证书验证
10. 使用代理
11. 超时
12. 身份验证
13. 将请求打包
#### Twisted网络框架
1. 异步编程模型
2. Reactor（反应堆）模式
3. Twisted实现时间戳客户端
4. Twisted实现时间戳服务端
--------------------------
### 解析库
#### 正则表达式
1. match：文本模式：match('文本模式'，'待匹配字符串')
2. search：查找模式：用法同上