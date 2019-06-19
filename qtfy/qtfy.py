from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import ip_tool

def get_movie(url, num):
	flag = True
	try:
		header = ip_tool.get_headers
		proxies = ip_tool.get_proxies()
		a = requests.get(url, headers=headers_raw_to_dict(header), proxies={'http': proxies})
		res = a.content


		if a.status_code != 200:
			raise Exception
		soup = BeautifulSoup(res, 'html.parser')
		result = soup.find_all('ul')[0].find_all('li')
		for i in result:

			cont = ('%s%s' % ('http://www.qtfy7.com', i.find('a').get('href')))
			b = requests.get(cont, headers=headers_raw_to_dict(header))
			data = b.content
			soup_data = BeautifulSoup(data, 'html.parser')
			result_down_url = soup_data.find_all(attrs={"class": "down_part_name"})

			for i in result_down_url:
				con = ('%s' % (str(i).split('"')[3],))
				save_url(con, num)
				break
		# print(result)
	except Exception as e:
			# print(e)
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

	po = Pool(3)

	for i in range(1, 500):
		url_res = url + str(i) + '.html'
		po.apply_async(get_movie, (url_res, str(i)))

	po.close()
	po.join()


def test():
    headers = ip_tool.get_headers()
    proxies = ip_tool.get_proxy()
    r = requests.get('https://www.xicidaili.com/nn/9', headers=headers, proxies={'http': proxies})
    print(r.status_code)

if __name__ == '__main__':
	main()

