from multiprocessing import Pool
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
import datetime
import random
import requests
import urllib
import csv


def xicidaili(url, msg):
	re_url = str(url.split('/')[4])
	jg = list()
	res_dict = {}
	file_name = str(msg) + '.csv'
	try:
		print('开始爬取第%s页...' % (re_url,))
		browser = webdriver.Chrome()
		time_num = int(random.uniform(50, 200))
		time.sleep(time_num)

		browser.get(url)

		pageSource = browser.page_source
		soup = BeautifulSoup(pageSource, 'html.parser')
		res = soup.find_all('tr')
		title = ['ip', 'port']

		csv_file = open(file_name, 'a', newline='')
		csv_write = csv.writer(csv_file, dialect='excel')
		csv_write.writerow(title)

		for  i in range(int(len(res))):
			jg.append(res[i].find_all('td'))


		for x in range(int(len(jg))):
			user_ip    = ''
			user_port  =  ''
			for i in range(int(len(jg[x]))):

				user_ip = str(jg[x][1].text).replace("\n","")
				if len(user_ip) == 0:
					user_ip = 'No'

				user_port  = str(jg[x][2].text).replace("\n","")
				if len(user_port) == 0:
					user_port = 'No'

			csv_write.writerow([user_ip, user_port])

	except Exception as e:
		print(e)
	finally:
		print('第%s页爬取完成!' % (re_url,))
		browser.close()

# def change_time(string):
# 	try:
# 		if '天' in string:
# 			temp_time = int(string.replace('天', ''))
# 			res_time = (temp_time * 24 * 60 * 60)
# 		elif '小时' in string:
# 			temp_time = int(string.replace('小时', ''))
# 			res_time = (temp_time * 60 * 60)
# 		elif '分钟' in string:
# 			temp_time = int(string.replace('分钟', ''))
# 			res_time = (temp_time * 60)

# 	except Exception as ret:
# 		print(ret)
# 	finally:
# 		return res_time


def main():
	# xicidaili("http://localhost/m/")
	po = Pool(25)
	# for i in range(1, 4):
	# url = 'http://localhost/m/'
	# url = 'https://www.xicidaili.com/nn/'
	# url = 'https://www.xicidaili.com/nt/'
	# url = 'https://www.xicidaili.com/wn/'

	url = 'https://www.xicidaili.com/wt/'
	for i in range(1,100):
		# print(url+str(i))

		tmp_url = url + str(i)
		po.apply_async(xicidaili, (str(tmp_url), str(i)))
	# 	# worker(str(i))

	# # print('-----start-----')
	po.close()
	po.join()
	# print('-----end-----')


if __name__ == '__main__':
	# test('19-05-15 20:21')
	main()
