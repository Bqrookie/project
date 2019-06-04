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

def get_all_list():
	url = 'http://www.qtfy7.com/vod-type-1-'
	# url_list = ['http://www.qtfy7.com/vod-type-1-1134.html']
	url_res = list()
	for i in range(1, 1135):
		url_res.append(url + str(i) + '.html')
	return url_res


def get_down_url(url):

	try:
		browser = webdriver.Chrome()
		# time.sleep(random.randint(20, 80))
		browser.get(url)
		# time.sleep(3)
		pageSource = browser.page_source
		# soup = BeautifulSoup(pageSource, 'html.parser')
		file_name = url.split('.')[2].split('-')[3] + '.txt'
		print(pageSource)
		# with open(file_name, 'w') as f:
		# 	f.write(pageSource)
		# result_down_url = soup.find_all('ul')[0].find_all('li')
		# print(result_down_url)
	except Exception as e:
		print(e)
	finally:
		browser.close()



def main():
	down_url = get_all_list()

	for item in down_url:
		get_down_url(item)
		exit()

if __name__ == '__main__':
	main()