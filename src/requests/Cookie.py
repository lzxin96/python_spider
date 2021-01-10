import requests

r1 = requests.get('http://www.baidu.com')
# 输出所有的Cookie
print(r1.cookies)

# 获取每一个Cookie
for key,value in r1.cookies.items():
    print(key,'=',value)

# 获取简书首页内容，定义了Host、User-Agent和Cookie请求字段
headers = {
    'Host':'www.jianshu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Cookie':'BIDUPSID=309304EB54DCA9011B43BF09CEF4A5BD; PSTM=1605785257; BAIDUID=309304EB54DCA90167278BA259BF3C1A:FG=1; BD_UPN=12314753; BDUSS=W5aTEUtUUJtMFlQRlBHLWtrWkx6T2Y1S1dGUjhibFhtRVN4Ni1GVFYyeG9YLU5mSVFBQUFBJCQAAAAAAAAAAAEAAAAzyFyE0KE4wK-xygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjSu19o0rtfa; BDUSS_BFESS=W5aTEUtUUJtMFlQRlBHLWtrWkx6T2Y1S1dGUjhibFhtRVN4Ni1GVFYyeG9YLU5mSVFBQUFBJCQAAAAAAAAAAAEAAAAzyFyE0KE4wK-xygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjSu19o0rtfa; __yjs_duid=1_9b55b27bc9446318edfc07d685fb0ae31609168835993; BAIDUID_BFESS=C5AFFAD48B930E129C05C0D65FABD335:FG=1; COOKIE_SESSION=602_0_8_1_50_18_0_0_3_5_0_5_896027_0_0_0_1610113878_0_1610114475%7C9%230_0_1610114475%7C1; BD_HOME=1; H_PS_PSSID=33423_33404_31254_33287_33413_26350_33267_33370; sug=3; sugstore=0; ORIGIN=0; bdime=0; BA_HECTOR=042l01a181a18lahmo1fvlogm0r'
}
# 请求简书首页，并通过headers参数发送cookie
r2 = requests.get('http://www.jianshu.com', headers=headers)
print(r2.text)

# 另外一种设置Cookie的方式
headers = {
    'Host':'www.jianshu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
}
cookies = 'BIDUPSID=309304EB54DCA9011B43BF09CEF4A5BD; PSTM=1605785257; BAIDUID=309304EB54DCA90167278BA259BF3C1A:FG=1; BD_UPN=12314753; BDUSS=W5aTEUtUUJtMFlQRlBHLWtrWkx6T2Y1S1dGUjhibFhtRVN4Ni1GVFYyeG9YLU5mSVFBQUFBJCQAAAAAAAAAAAEAAAAzyFyE0KE4wK-xygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjSu19o0rtfa; BDUSS_BFESS=W5aTEUtUUJtMFlQRlBHLWtrWkx6T2Y1S1dGUjhibFhtRVN4Ni1GVFYyeG9YLU5mSVFBQUFBJCQAAAAAAAAAAAEAAAAzyFyE0KE4wK-xygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjSu19o0rtfa; __yjs_duid=1_9b55b27bc9446318edfc07d685fb0ae31609168835993; BAIDUID_BFESS=C5AFFAD48B930E129C05C0D65FABD335:FG=1; COOKIE_SESSION=602_0_8_1_50_18_0_0_3_5_0_5_896027_0_0_0_1610113878_0_1610114475%7C9%230_0_1610114475%7C1; BD_HOME=1; H_PS_PSSID=33423_33404_31254_33287_33413_26350_33267_33370; sug=3; sugstore=0; ORIGIN=0; bdime=0; BA_HECTOR=042l01a181a18lahmo1fvlogm0r'
# 额外设置cookies需要创建RequestCookieJar对象
jar = requests.cookies.RequestsCookieJar()
# 将多个Cookie拆开，多个Cookie之间用分号；分割
for cookie in cookies.split(';'):
    # 得到Cookie的key和value，每一个Cookie的key和value之间用等号=分隔
    key, value = cookie.split('=',1) 
    # 将Cookie添加到RequestsCookieJar对象中
    jar.set(key,value)
# 请求简书首页，并通过cookies参数发送Cookie
r3 = requests.get('http://www.jianshu.com', cookies=jar, headers=headers)
print(r3.text)