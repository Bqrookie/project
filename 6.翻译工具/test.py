"""
通过查找，能找到js代码中的操作代码
1.这是计算salt的公式，在fanyi.min.js文件中找到的，
t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
2.sign: n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
md5一共需要四个参数，第一个和第四个都是固定的字符串，第三个是所谓的salt。第二个就是输入的要查找的单词
"""

def getSalt():
    """
    这是计算salt的公式  "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
    把它翻译成Python代码
    :return:
    """
    import time,random
    # (new Date).getTime()生成的时间戳与time.time()的单位不一致，所以需要乘1000
    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMd5(v):
    import hashlib
    md5 = hashlib.md5()

    # 需要一个bytes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign

def getSign(key, salt):
    sign = "fanyideskweb" + key + str(salt) + "sr_3(QOHT)L2dx#uuGR@r"
    sign = getMd5(sign)
    return sign

from urllib import request,parse

def youdao(key):

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = getSalt()
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
        "typoResult": "false",
    }
    print(data)
    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode('utf-8')
    headers = {
        "Accept": "application/json,text/javascript,*/*;q=0.01",
        # "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        # "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1076696971@10.168.8.63;JSESSIONID=aaaZ6s5m9DVmYf8g3QoDw;OUTFOX_SEARCH_USER_ID_NCOO=473292646.5080033;___rl__test__cookies=1543228484656",
        "Host": "fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.100Safari/537.36OPR/56.0.3051.104X-Requested-With:XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode('utf-8')
    # for values in html["translateResult"]:
    #     print(values)

    print(html)

if __name__ == '__main__':
    youdao("girl")
