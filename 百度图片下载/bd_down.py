import ip_tool
import requests
import json
import os
import time
import random


def get_proxies_headers():
    # 获取一个代理，格式为ip:端口
    proxies = ip_tool.get_proxies()
    # 获取一个随机user_agent
    headers = ip_tool.get_headers()

    return proxies, headers


def get_image(word, num):

    file_path = 'C:/Users/Administrator/Desktop/Git/project/百度图片下载/' + word + '/'
    isExists = os.path.exists(file_path)

    if not isExists:
        os.mkdir(file_path)

    proxies, headers = get_proxies_headers()
    this_headers = {
        'Host': 'image.baidu.com'
    }
    headers = dict(this_headers, **headers)

    num = (num-1)*30

    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexnew&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&face=0&istype=2&qc=&nc=1&fr=&pn=%s&rn=30' % (word, str(num))


    try:
        # 使用代理访问
        req = requests.get(url, proxies={"http": proxies}, timeout=5, headers=headers)
        # 没有报异常，说明访问成功
        # 获得返回数据
        if req.status_code == 200:
            result_list = json.loads(req.text)['data']
            result_list = result_list[:len(result_list)-1]
            for item in result_list:
                os.chdir(file_path)
                now = int(time.time())
                tmp_name = str(random.randint(1000000,9999990)) + str(now)
                file_name = file_path + tmp_name + '.' + item['type']
                r = requests.get(item['thumbURL'])

                with open(file_name, 'wb') as f:
                    f.write(r.content)

    except Exception as msg:
        print("fun:get_image【%s】" % (msg,))


def main():

    # 设置搜索关键字
    search_work = 'apple'

    # 设置需要下载图片的页数
    pages = 3

    for i in range(1, pages+2):
        get_image(search_work, i)


if __name__ == '__main__':
    main()
