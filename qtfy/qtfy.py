from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import urllib
import csv
import time
import random

from copyheaders import headers_raw_to_dict


def get_movie(url, num):
	flag = True
	try:
		header = b'''Host: www.qtfy7.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
DNT: 1
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://www.qtfy7.com/?security_verify_data=313932302c31303830
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7
Cookie: UM_distinctid=16a120628db11b-0b0a54138372d7-e323069-144000-16a120628dc32d; CNZZDATA1273797313=428397387-1556020400-null%7C1558946407; PHPSESSID=0tbl42chtrt5eihuplvlbjgov2; Hm_lvt_3d1aa03b722039def5db91556769ec08=1559186273,1559275864,1559287255,1559486681; mac_history=%7Bvideo%3A%5B%7B%22name%22%3A%22%u8349%u8393%u4E4B%u591C%B7%u82F1%u96C4%u4F20%22%2C%22link%22%3A%22/content-24505.html%22%2C%22typename%22%3A%22%u5267%u60C5%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-04-12/201904121555066807.jpg%22%7D%2C%7B%22name%22%3A%22%u4E27%u5C38%u672A%u901D%22%2C%22link%22%3A%22/content-24914.html%22%2C%22typename%22%3A%22%u6050%u6016%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-06-01/201906011559398805.jpg%22%7D%2C%7B%22name%22%3A%22%u5C11%u5E74%u72AF2018%22%2C%22link%22%3A%22/content-24927.html%22%2C%22typename%22%3A%22%u5267%u60C5%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-06-02/201906021559459991.jpg%22%7D%2C%7B%22name%22%3A%22%u4FD8%u864F%u56FD%u5EA6%22%2C%22link%22%3A%22/content-24918.html%22%2C%22typename%22%3A%22%u79D1%u5E7B%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-06-02/201906021559441494.jpg%22%7D%2C%7B%22name%22%3A%22%u5927%u4FA0%u522B%u80E1%u6765%22%2C%22link%22%3A%22/content-24929.html%22%2C%22typename%22%3A%22%u5267%u60C5%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-06-03/201906031559520500.jpg%22%7D%2C%7B%22name%22%3A%22%u5FB7%u4E91%u793E%u5CB3%u4E91%u9E4F%u76F8%u58F0%u4E13%u573A%u5927%u8FDE%u7AD92019%22%2C%22link%22%3A%22/content-24930.html%22%2C%22typename%22%3A%22%u5267%u60C5%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-06-03/201906031559523019.jpg%22%7D%2C%7B%22name%22%3A%22%u5C0F%u9547%u53CD%u9762%22%2C%22link%22%3A%22/content-336.html%22%2C%22typename%22%3A%22%u52A8%u4F5C%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22http%3A//img.qtfy7.com/pic/uploadimg/2016-6/393.jpg%22%7D%2C%7B%22name%22%3A%22%u6559%u5B98%u65BD%u5BC6%u7279%22%2C%22link%22%3A%22/content-340.html%22%2C%22typename%22%3A%22%u52A8%u4F5C%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22http%3A//img.qtfy7.com/pic/uploadimg/2016-6/398.jpg%22%7D%2C%7B%22name%22%3A%22%u9003%u5B66%u5A01%u9F992%22%2C%22link%22%3A%22/content-3872.html%22%2C%22typename%22%3A%22%u559C%u5267%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22http%3A//img.qtfy7.com/pic/uploadimg/2016-6/4402.jpg%22%7D%2C%7B%22name%22%3A%22%u590D%u4EC7%u8005%u8054%u76DF3%uFF1A%u65E0%u9650%u6218%u4E89%22%2C%22link%22%3A%22/content-21983.html%22%2C%22typename%22%3A%22%u79D1%u5E7B%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22http%3A//img.qtfy7.com/pic/uploadimg/2019-2/25664.jpg%22%7D%2C%7B%22name%22%3A%22%u732B%u7247%u4E4B%u65E0%u55B5%u751F%u8FD8%22%2C%22link%22%3A%22/content-24841.html%22%2C%22typename%22%3A%22%u5267%u60C5%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22https%3A//img.tupian-zuida.com/pic/upload/vod/2019-05-26/201905261558879960.jpg%22%7D%2C%7B%22name%22%3A%22%u8718%u86DB%u4FA03%22%2C%22link%22%3A%22/content-5279.html%22%2C%22typename%22%3A%22%u52A8%u4F5C%u7247%22%2C%22typelink%22%3A%22/vod-type--1.html%22%2C%22pic%22%3A%22http%3A//img.qtfy7.com/pic/uploadimg/2016-6/6049.jpg%22%7D%5D%7D; CNZZDATA1276470099=1934195665-1555079324-%7C1559551822; Hm_lpvt_3d1aa03b722039def5db91556769ec08=1559553312
'''
		a = requests.get(url, headers=headers_raw_to_dict(header))
		res = a.content

		if a.status_code != 200:
			raise Exception
		soup = BeautifulSoup(res, 'html.parser')
		result = soup.find_all('ul')[0].find_all('li')
		for i in result:
			# time.sleep(random.randint(20, 50))

			cont = ('%s%s' % ('http://www.qtfy7.com', i.find('a').get('href')))
			b = requests.get(cont, headers=headers_raw_to_dict(header))
			data = b.content
			soup_data = BeautifulSoup(data, 'html.parser')
			result_down_url = soup_data.find_all(attrs={"class": "down_part_name"})
			#attrs={"name": "down_url_list_0"}) #name='down_url_list_0')
			# print(result_down_url)
			# if result_down_url:
			for i in result_down_url:
				# data_soup = BeautifulSoup(i)
				con = ('%s' % (str(i).split('"')[3],))
				save_url(con, num)
				# print(str(i).split('"')[5])
				break
			# 	print(result_down_url[0])

			# print(result_down_url)
		# print(result)
	except Exception as e:
			# print(ip)
		print('%s爬取失败，error【%s】' % (url, e))
		flag = False
	finally:
		if flag:
			print('[%s]爬取完成' % (url,))


def save_url(url, num):
	file_name = str(num) + '.txt'
	with open(file_name, 'a') as f:
		f.write(url + '\n')


def main():
	url = 'http://www.qtfy7.com/vod-type-1-'
	# url_list = ['http://www.qtfy7.com/vod-type-1-1134.html']

	po = Pool(20)

	for i in range(99,500):
		url_res =  url + str(i) + '.html'
		# po.apply_async(get_movie, (url_res, str(i)))
		time.sleep(random.randint(10,50))
		get_movie(url_res, str(i)) # po.apply_async((url_res, str(i)))
		# print(url_res)

	po.close()
	po.join()


if __name__ == '__main__':
	main()

