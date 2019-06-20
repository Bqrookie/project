import requests
import ip_tool
import queue
import threading
from bs4 import BeautifulSoup
import csv

# 创建一个队列
page_queue = queue.Queue(1134)

# 创建一个线程锁，防止多线程写入文件时发生错乱
# mutex_lock = threading.Lock()

out = open('qtfy.csv', 'a+', newline='')
csv_write = csv.writer(out, dialect='excel')

def get_all_page():
	"""
	获取所有页面
	:return:
	"""

	page_list = list()
	url = 'http://www.qtfy7.com/vod-type-1-'
	# url_list = ['http://www.qtfy7.com/vod-type-1-1134.html']

	for i in range(1, 1135):
		url_res = url + str(i) + '.html'
		page_list.append(url_res)

	return page_list


def get_video_list():
	# print('1')
	"""
	获取每个页面的电视链接
	:return:
	"""
	# 当队列不为空时
	while (not page_queue.empty()):
		tmp_url = 'http://www.qtfy7.com'

		# 从队列读取一个基金代码
		# 读取是阻塞操作
		this_page = page_queue.get()
		# 获取一个代理，格式为ip:端口
		proxies = ip_tool.get_proxies()
		# 获取一个随机user_agent
		headers = ip_tool.get_headers()
		# 使用try、except来捕获异常
		# 如果不捕获异常，程序可能崩溃
		try:
			# 使用代理访问
			req = requests.get(this_page, proxies={"http": proxies}, timeout=5, headers=headers)
			# print(1)

			# 没有报异常，说明访问成功
			# 获得返回数据
			if req.status_code == 200:
				soup = BeautifulSoup(req.text, "html.parser")

				tag = soup.find_all('h2')
				for item in tag:
					video_link = tmp_url + item.a.get('href')
					get_down_url(video_link)
				break
			else:
				# 访问异常直接抛出重新采集
				raise Exception
		except Exception as msg:
			# 访问失败了，所以要把我们刚才取出的数据再放回去队列中
			page_queue.put(this_page)
			print("get_video_list【%s】" % (msg))


def get_down_url(link):
	while True:
		try:
			tmp = requests.get(link, proxies={"http": ip_tool.get_proxies()}, timeout=15, headers=ip_tool.get_headers())
			if tmp.status_code == 200:
				ss = BeautifulSoup(tmp.text, "html.parser")
				down_link = ss.select('.down_part_name')
				for item in down_link:
					item_href = item.a.get('href')
					item_name = item.a.text

					# 申请获取锁，此过程为阻塞等待状态，直到获取锁完毕
					# mutex_lock.acquire()
					# 追加数据写入csv文件，若文件不存在则自动创建
					result = [item_name, item_href]
					csv_write.writerow(result)
					# 释放锁
					# mutex_lock.release()
					print('%s 采集完成' % (link,))
				break
		except Exception as e:
			print('get_down_url[%s]' % (e,))


def main():
	# 获取所有页面
	url_list = get_all_page()
	# 将所有页面放入先进先出的队列中
	# 队列的写入和读取都是阻塞的，故在多线程情况下不会乱
	# 在不使用框架的前提下，引入多线程，提高爬取效率

	# 写入页面数据到队列
	for i in range(len(url_list)):
		page_queue.put(url_list[i])

	# 线程数为50，在一定范围内，线程数越多，速度越快
	for i in range(150):
		t = threading.Thread(target=get_video_list)
		t.start()


if __name__ == '__main__':
	main()
