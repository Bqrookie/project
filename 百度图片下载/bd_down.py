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


def get_image(word, num, file_path):

    is_exists = os.path.exists(file_path)

    # 判断目录是否存在
    if not is_exists:
        # 不存在就创建
        os.mkdir(file_path)

    proxies, headers = get_proxies_headers()
    this_headers = {
        'Host': 'image.baidu.com'
    }
    headers = dict(this_headers, **headers)

    # 就是留个数字做输出展示
    tmp = num
    # 根据页数设置pn的值
    num = (num-1)*30

    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&catename=pcindexnew&ipn=rj&ct=201326592&is=&fp\
=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&face=0&istype=\
2&qc=&nc=1&fr=&pn=%s&rn=30' % (word, str(num))

    try:
        # 使用代理访问
        req = requests.get(url, proxies={"http": proxies}, timeout=5, headers=headers)
        # 没有报异常，说明访问成功
        # 获得返回数据
        if req.status_code == 200:
            # 通过转换，修正编码错误
            res = json.loads(req.text.replace('\/', '/').replace(r"\'", ''))
            # print(req)
            res = res['data']
            res = res[:len(res) - 1]
            for item in res:
                tmp_name = str(random.randint(1, 999)) + str(time.time())
                file_name = file_path + tmp_name + '.' + item['type']
                r = requests.get(item['thumbURL'])

                with open(file_name, 'wb') as f:
                    f.write(r.content)

            print('第%s页采集完成' % (tmp,))

    except Exception as msg:
        print("fun:get_image【%s】" % (msg,))


def main():

    # 设置搜索关键字
    # search_work = '动漫头像'
    search_work = str(input('pic > '))

    # 设置需要下载图片的页数
    # pages = 10
    pages = int(input('pages> '))

    # 设置下载目录
    file_path = 'C:/Users/Administrator/Desktop/' + search_work + '/'
    for i in range(1, pages+1):
        get_image(search_work, i, file_path)


if __name__ == '__main__':
    main()
