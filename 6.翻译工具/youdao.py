import requests
import hashlib
import random
import time
import json
from urllib import request,parse
import ResponseTool as myTool

def main():
	fy = '中国'
	do_work(fy)


def do_work(fy):

	headers={
		# "Host": "fanyi.youdao.com",
		# "Connection": "keep-alive",
		# "Content-Length": "282",
		# "Accept": "application/json, text/javascript, */*; q=0.01",
		# "Origin": "http://fanyi.youdao.com",
		# "X-Requested-With": "XMLHttpRequest",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
		# "DNT":"1",
		# "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Referer": "http://fanyi.youdao.com/",
		# "Accept-Encoding": "gzip, deflate",
		# "Accept-Language": 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
		"Cookie": "OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;",
}
	app_ver = "5.0 (Windows NT 6.2; rv:51.0) Gecko/20100101 Firefox/51.0"

	ts = int(time.time()*1000)
	num1 = int(random.random() * 10)
	salt1 = str(ts+num1)
	print(salt1)

	salt = int(time.time() * 1000) + random.randint(0, 10)
	print(salt)

	a = "fanyideskweb"
	b = fy
	c = salt
	d = "@6f#X3=cCuncYssPsuRUE"
	res_sign = a + b + str(c) + d

	m1 = hashlib.md5()
	m1.update(res_sign.encode('utf-8'))
	sign = m1.hexdigest()

	aaa = hashlib.md5()
	aaa.update(app_ver.encode("utf-8"))
	bv = aaa.hexdigest()

	form_data = {
				"type" : "AUTO",
        "i" : fy,
        "doctype" : "json",
        "xmlVersion" : "1.8",
        "keyfrom" : "fanyi.web",
        "ue" : "UTF-8",
        "action" : "FY_BY_CLICKBUTTON",
        "typoResult" : "true"
				}
	# form_data = parse.urlencode(form_data).encode('utf-8')
	# print(headers['User-Agent'])


	req_url = "http://fanyi.youdao.com/translated?smartresult=dict&smartresult=rule"
	# print(myTool.ResponseTool().proxies)
	req = requests.get(req_url, data=form_data, headers=headers)#, proxies={"http": myTool.ResponseTool().proxies})
	with open ('1.html', 'wb') as f:
		f.write(req.content)

	print(req.content)


if __name__ == '__main__':
	main()
