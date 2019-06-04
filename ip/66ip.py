from multiprocessing import Pool
from bs4 import BeautifulSoup
import requests
import urllib
import csv

from copyheaders import headers_raw_to_dict

def get_ip(url, num):
    try:
        # print('开始爬取[%s]' % (url,))
        header = b'''Host: www.66ip.cn
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
DNT: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7
Cookie: __jsluid=c2987915dbe65f79e0c316e5d1641f61; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1558324410,1558336044,1559483256; __jsl_clearance=1559531474.453|0|FYsh%2FacRIjeP6oUmkKUaXf8G90c%3D; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1559531478'''
        a = requests.get(url, headers=headers_raw_to_dict(header))
        res = a.content.decode('gbk')

        soup = BeautifulSoup(res, 'html.parser')
        result = soup.find_all('table')[2].find_all('tr')[1:]
        # print(soup)
        file_name = str(num) + '.csv'

        title = ['ip', 'port']
        csv_file = open(file_name, 'a', newline='')
        csv_write = csv.writer(csv_file, dialect='excel')
        csv_write.writerow(title)
        for i in result:
            # cont = ('%s:%s' % (i.find_all('td')[0].text, i.find_all('td')[1].text))
            csv_write.writerow([i.find_all('td')[0].text, i.find_all('td')[1].text])
            # print(i)
    except Exception as e:
        print(e)
    finally:
        print('[%s]爬取完成' % (url,))

def main():
    
    url_list = ["http://www.66ip.cn/areaindex_1/1.html","http://www.66ip.cn/areaindex_2/1.html",
               "http://www.66ip.cn/areaindex_3/1.html",
               "http://www.66ip.cn/areaindex_4/1.html",
               "http://www.66ip.cn/areaindex_5/1.html",
               "http://www.66ip.cn/areaindex_6/1.html",
               "http://www.66ip.cn/areaindex_7/1.html",
               "http://www.66ip.cn/areaindex_8/1.html",
               "http://www.66ip.cn/areaindex_9/1.html",
               "http://www.66ip.cn/areaindex_10/1.html",
               "http://www.66ip.cn/areaindex_11/1.html",
               "http://www.66ip.cn/areaindex_12/1.html",
               "http://www.66ip.cn/areaindex_13/1.html",
               "http://www.66ip.cn/areaindex_14/1.html",
               "http://www.66ip.cn/areaindex_15/1.html",
               "http://www.66ip.cn/areaindex_16/1.html",
               "http://www.66ip.cn/areaindex_17/1.html",
               "http://www.66ip.cn/areaindex_18/1.html",
               "http://www.66ip.cn/areaindex_19/1.html",
               "http://www.66ip.cn/areaindex_20/1.html",
               "http://www.66ip.cn/areaindex_21/1.html",
               "http://www.66ip.cn/areaindex_22/1.html",
               "http://www.66ip.cn/areaindex_23/1.html",
               "http://www.66ip.cn/areaindex_24/1.html",
               "http://www.66ip.cn/areaindex_25/1.html",
               "http://www.66ip.cn/areaindex_26/1.html",
               "http://www.66ip.cn/areaindex_27/1.html",
               "http://www.66ip.cn/areaindex_28/1.html",
               "http://www.66ip.cn/areaindex_29/1.html",
               "http://www.66ip.cn/areaindex_30/1.html",
               "http://www.66ip.cn/areaindex_31/1.html",
               "http://www.66ip.cn/areaindex_32/1.html",
               "http://www.66ip.cn/areaindex_33/1.html",
               "http://www.66ip.cn/areaindex_34/1.html"]

    po = Pool(5)

    num = 1
    for url in url_list:
        po.apply_async(get_ip, (url, num))
        # print(url)
        num += 1

    po.close()
    po.join()


if __name__ == '__main__':
    main()

