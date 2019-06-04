import requests
import csv
from multiprocessing import Pool
import urllib

def main():

	res_list = get_data()
	po = Pool(100)
	for url in res_list:
		po.apply_async(verification, (url,))


	po.close()
	po.join()



def verification(ip):
	# res = requests.get('http://bqrookie.com/', ip)
	try:
		proxy_support = urllib.request.ProxyHandler({'http': ip})

		opener = urllib.request.build_opener(proxy_support)
		opener.addheaders = [('User-Agent',
							  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0')]
		urllib.request.install_opener(opener)
		response = urllib.request.urlopen('http://icanhazip.com/')
		html = response.read().decode('utf-8')
		# if response.getcode() == 200:
		# 	print(ip)
		if html in ip:
			print(ip)
	except Exception as e:
		print('fn:verification: %s' % (e,))
	finally:
		return 0

def get_data():
	file_name = 'all-in-one.csv'
	csv_file = csv.reader(open(file_name))
	ip_list = list()
	for item in csv_file:
		ip_list.append('%s:%s' % (item[0], item[1]))
		# ip_list.append(item)

	return ip_list

if __name__ == '__main__':
	main()