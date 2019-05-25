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

import threadpool

def te(url):

    try:
        time.sleep(60)
        start_time = time.time()
        headers = {'user-agent': 'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'}
        r = requests.get(url, headers=headers)
        file_name = str(url).split('/')[4] + '.html'
        if r.status_code == 200:
            # print('OK!')
            with open(file_name, 'wb') as f:
                f.write(r.content)
        elif r.status_code == 503:
            # print('被封IP！')
            with open('error.log', 'a+') as f:
                f.write(str(file_name))
                f.write(' ')
    except Exception as e:
        print(e)
    finally:
        print('%d second'% (time.time()-start_time))


def main():


    name_list =list()
    for i in range(1,3684):
       url = 'https://www.xicidaili.com/nn/'
       name_list.append(url + str(i))    
    
    pool = threadpool.ThreadPool(20) 
    requests = threadpool.makeRequests(te, name_list) 
    [pool.putRequest(req) for req in requests] 
    pool.wait() 
    



if __name__ == '__main__':
    # test('19-05-15 20:21')
    main()
