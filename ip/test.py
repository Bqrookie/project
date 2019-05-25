from multiprocessing import Pool
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
import datetime
import random
import requests
import request
import urllib
import csv

import threadpool


def xicidaili(url):
    jg = list()
    res_dict = {}
    file_name = str(url).split('/')[4] + '.csv'
    try:
        time.sleep(50)
        browser = webdriver.Chrome()

        browser.get(url)

        time.sleep(3)

        pageSource = browser.page_source
        soup = BeautifulSoup(pageSource, 'html.parser')
        res = soup.find_all('tr')
        title = ['ip', 'port', '地址', '是否匿名', '类型', '存活时间', '验证时间']

        csv_file = open(file_name, 'a', newline='')
        csv_write = csv.writer(csv_file, dialect='excel')
        csv_write.writerow(title)

        for  i in range(int(len(res))):
            jg.append(res[i].find_all('td'))


        for x in range(int(len(jg))):
            user_ip    = ''
            user_port  =  ''
            user_addr  =  ''
            user_isnn=  ''
            user_type  =  ''
            user_over_time=  ''
            user_time=  ''
            for i in range(int(len(jg[x]))):

                user_ip = str(jg[x][1].text).replace("\n","") 
                if len(user_ip) == 0:
                    user_ip = 'No'

                user_port  = str(jg[x][2].text).replace("\n","")
                if len(user_port) == 0:
                    user_port = 'No'

                user_addr  = str(jg[x][3].text).replace("\n","")
                if len(user_addr) == 0:
                    user_addr = 'No'

                user_isnn= str(jg[x][4].text).replace("\n","")
                if len(user_isnn) == 0:
                    user_isnn = 'No'

                user_type  = str(jg[x][5].text).replace("\n","")
                if len(user_type) == 0:
                    user_type = 'No'

                user_over_time= str(jg[x][8].text).replace("\n","")
                if len(user_over_time) == 0:
                    user_over_time = 'No'
                else:
                    user_over_time = change_time(str(user_over_time))

                user_time= str(jg[x][9].text).replace("\n","") + ':00'
                if len(user_time) < 3:
                    user_time = 'No'


            csv_write.writerow([user_ip, user_port, user_addr, user_isnn, user_type, user_over_time, user_time])

    except Exception as e:
        print(e)
    finally:
        
        browser.close()

def change_time(string):
    try:
        if '天' in string:
            temp_time = int(string.replace('天', ''))
            res_time = (temp_time * 24 * 60 * 60)
        elif '小时' in string:
            temp_time = int(string.replace('小时', ''))
            res_time = (temp_time * 60 * 60)
        elif '分钟' in string:
            temp_time = int(string.replace('分钟', ''))
            res_time = (temp_time * 60)

    except Exception as ret:
        print(ret)
    finally:
        return res_time


def main():


    name_list =list()
    for i in range(1,101):
       url = 'http://localhost/m/'
       name_list.append(url + str(i))
    
    start_time = time.time()
    pool = threadpool.ThreadPool(20) 
    requests = threadpool.makeRequests(xicidaili, name_list) 
    [pool.putRequest(req) for req in requests] 
    pool.wait() 
    print('%d second'% (time.time()-start_time))


def ttt():
    try:
        
        #访问网址
        url = 'http://icanhazip.com/'
        #这是代理IP
        # proxies = [{'http':'47.104.179.65:8081'}]
        r = requests.get(url=url,proxies={'http':'167.99.231.73:8080'}, timeout=5)
        print(r.status_code)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # test('19-05-15 20:21')
    # main()
    ttt()
