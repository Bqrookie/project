import FindWork as Fw
import requests
from bs4 import BeautifulSoup
import csv





def main():

	# 展示选择信息
	local_url, local_job = show()
	# print(local_url)
	get_max_page(local_url, find_work.MyTool.url_conversion(local_job, True))


def get_max_page(local_url, local_job):
	num = 1
	res_url = local_url + "pn" + str(num) + "/?key=" + find_work.MyTool.url_conversion(local_job, True) + "&final=1&jump=1"
	# 保存一个副本，生成list
	tmp_url = res_url[:]
	try:
		# print(find_work.MyTool.proxies)
		# print(find_work.MyTool.headers)
		req = requests.get(tmp_url, proxies={"https": find_work.MyTool.proxies}, timeout=5, headers=find_work.MyTool.headers)
		# print(req)
		if req.status_code == 200:
			print(req.text)
	except Exception as msg:
		print('fn[get_max_page][%s]' % (msg,))


def show():
	"""展示选择信息"""
	tmp_url = ''

	for item in pro:
		print(item, end=' ')
	print()
	# 先获取某个省的所有城市url
	input_pro = '广东'#input('请输入省份：')
	pro_city_urls = get_pro_city(input_pro)
	if pro_city_urls != 'No_Data':
		for item in pro_city_urls:
			print(item, end=' ')

		print()
		input_city = '肇庆'#input('请输入城市：')
		city_urls = get_pro_city(input_pro, input_city)
		tmp_url = city_urls
	else:
		print('找不到')
		exit(0)

	tmp_job = '服务员'#input('请输入职业:')

	return tmp_url, tmp_job


def get_pro_city(input_pro, input_city=None):
	"""根据省份返回该省城市链接列表"""
	if input_city == None:
		for item in pro:
			if item == input_pro:
				return pro[item]
		return 'No_Data'

	try:
		result = pro[input_pro][input_city]
		return result
	except Exception as e:
		print('找不到该城市')
		exit(0)


if __name__ == '__main__':
	find_work = Fw.FindWork()
	pro = find_work.citys

	main()
"""
out = open('58_job.csv', 'a+', newline='')
csv_write = csv.writer(out, dialect='excel')
ti_list = ['更新时间', '浏览人数', '申请人数', '薪水', '福利待遇', '应聘要求', '职位', '职称', '上班地址', '职位描述', '工作超链接']
csv_write.writerow(ti_list)

def main():

	req_url = ''

	for item in citys:
		print(item, end=' ')

	print()
	input_pro = '广东' #input('请选择省份：')
	for item in citys[input_pro]:
		print(item.split('-')[0], end=' ')

	print()
	input_city = '广州' # input('请选择城市：')
	for city in citys[input_pro]:
		if city.split('-')[0] == input_city:
			req_url = city.split('-')[1]

	input_job = '服务员' # input('请选择职位：')
	res_url = req_url[:]
	# req_url = req_url + '/pn1/?key=' + input_job + '&final=1&jump=1'

	do_work(res_url, find_work)
	print('do_work end')
	get_job()
	print('get_job end')



def do_work(url, find_work):
	try:
		# 使用代理访问
		req = requests.get(url, proxies={"http": find_work.MyTool.proxies}, timeout=5, headers=find_work.MyTool.headers)

		if req.status_code == 200:
			soup = BeautifulSoup(req.text, 'html.parser')
			max_page = int(soup.select('span', attrs={'class=total_page'})[4].get_text())
			# print(max_page)
			for item in range(1, max_page+1):
				tmp_url = url + 'pn' + str(item) + "/?key=%E6%9C%8D%E5%8A%A1%E5%91%98&final=1&jump=1"
				find_work.url_queue.put(tmp_url)
				print(tmp_url)

			print('url采集完成')

		else:
			# 访问异常直接抛出
			raise Exception
	except Exception as msg:
		print("fun:do_work=>status_code【%s】【%s】" % (req.status_code, msg))


def get_job():

	while not find_work.url_queue.empty():

		local_url = find_work.url_queue.get()
		try:
			# 使用代理访问
			req = requests.get(local_url, proxies={"http": find_work.MyTool.proxies}, timeout=5,
							   headers=find_work.MyTool.headers)

			if req.status_code == 200:
				soup = BeautifulSoup(req.text, 'html.parser')
				test = soup.select('div.job_name a')
				for item in test:
					if 'courseinfoid' not in str(item):
						result = requests.get(item.get('href'), proxies={"http": find_work.MyTool.proxies}, timeout=5,
											  headers=find_work.MyTool.headers)
						# print(result.text)
						result_soup = BeautifulSoup(result.text, 'html.parser')
						# result = result_	soup.select('div.leftCon')
						update = result_soup.select('span.pos_base_num')

						# 更新时间
						update_time = str(update[0].get_text())[4:]

						# 浏览人数
						tt = str(update[1].get_text())
						look_num = tt[3:len(tt)-1].lstrip().rstrip()

						# 申请人数d
						yy = str(update[2].get_text())
						shenqing_num = yy[3:len(yy)-1].lstrip().rstrip()

						yuexin = result_soup.select('span.pos_salary')

						# 薪水
						money = yuexin[0].get_text()
						if len(money) > 4:
							money = money[:len(money)-3]

						dy = result_soup.select('div.pos_welfare')
						dy_list = list()
						for i in dy:
							dy_list.append(i.get_text())
						# print(dy_list)

						# 福利待遇
						dy_res = str(dy_list).replace('[\'', '').replace('\']', '')
						if len(dy_res) == 0:
							dy_res = '无'
						dy_list.clear()


						yq = result_soup.select('div.pos_base_condition')
						yq_list = list()
						for i in yq:
							yq_list.append(i.get_text())

						# 应聘要求
						yq_res = str(yq_list).replace('[\'', '').replace('\']', '')
						if len(yq_res) == 0:
							yq_res = '无'
						# print(yq_res)
						yq_list.clear()


						dz = result_soup.select('div.pos-area span')
						dz.pop()

						dz_res = str(dz.pop())
						# 上班地址
						last_res_dz = str(dz_res)[6:len(str(dz_res))-7]

						# 职称
						pos_title = result_soup.select('span.pos_title')
						pos_title_res = str(pos_title[0])[24:len(str(pos_title[0]))-7].lstrip().rstrip()
						# 职位
						pos_name = result_soup.select('span.pos_name')
						pos_name_res = str(pos_name[0])[23:len(str(pos_name[0]))-7].lstrip().rstrip()
						# print("%s-%s" % (pos_title, pos_name))

						# 职位描述
						des = result_soup.select('div.des')
						des_res = str(des[0])[17:].replace('</div>', '').replace('<br/>', '')

						# 更新时间 浏览人数 申请人数 薪水 福利待遇 应聘要求 职位 职称 上班地址 职位描述 工作超链接
						result_last = [update_time, look_num, shenqing_num, money, dy_res, yq_res, pos_name_res, pos_title_res, last_res_dz, des_res, local_url]
						csv_write.writerow(result_last)

						print('%s采集完成' % (local_url,))

			else:
				# 访问异常直接抛出
				raise Exception
		except Exception as msg:
			find_work.url_queue.put(local_url)
			print("fun:do_get=>status_code【%s】【%s】" % (req.status_code, msg))


if __name__ == '__main__':
	main()

citys = find_work.citys['citys']

"""