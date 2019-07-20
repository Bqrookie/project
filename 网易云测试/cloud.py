# -*- coding: utf-8 -*-
import ResponseTool as ip_tool
import requests
from bs4 import BeautifulSoup
import json
import os
import time
import random
import queue
import threading
import traceback


def get_singers_pages_url():
    """
    获取所有歌手爬取页面
    :return:
    """
    url_singer_type = url + '/discover/artist'
    try:
        req = requests.get(url_singer_type, proxies={"http": proxies}, headers=headers)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            tag_blk = soup.select('.blk')
            tag_blk.pop()

            for tab in tag_blk:

                # 循环获取歌手类型的超链接
                for detail in tab.select('a'):

                    # 获取所有歌手类型的链接
                    url_type = url + detail.get('href')

                    initial = [0, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                    
                    for url_initial in initial:
                        
                        # 通过拼接生成每种类型歌手的所有抓取页面 A-Z开头的所有歌手
                        get_all_singer_pages.append("%s&initial=%s" % (url_type,str(url_initial)))

                    print('%s页面爬取成功' % (detail.text,))
                    # break # DEBUG 测试仅仅循环一次
                # break # DEBUG 测试仅仅循环一次

    except Exception as msg:
        print('get_all_singer_type[%s]' % msg)


def get_all_singer_user_page():
    """
    先爬取所有歌手ID
    通过拼接生成歌手主页链接
    获取所有歌手专辑页面
    :return:
    """
    try:
        num = 1
        for i in get_all_singer_pages:
            req = requests.get(i, proxies={"http": proxies}, headers=headers)
            if req.status_code == 200:
                get_singer = BeautifulSoup(req.text, 'html.parser')
                singers = get_singer.find_all(attrs={'class': 'nm nm-icn f-thide s-fc0'})

                for i in singers:
                    url_singer_page = 'https://music.163.com/artist/album?id='
                    if '/user/home' not in str(i):
                        url_singer_page = url_singer_page + str(i.get('href').split('=')[1]) + str(
                            '&limit=600&offset=0')

                        # tmp = str(i.get('href').split('=')[1]) + str('&limit=600&offset=0')
                        tmp = str(i.get('href').split('=')[1])

                        with open('txt', 'a') as f:
                            f.write(str(tmp) + '-')

                        # singer_user_pages.append(url_singer_page)

                        # print('歌手[%s] 已采集' % str(i.text))
               # break  # DEBUG 测试时候仅仅循环一次
            print('共%s页已爬取%s页' % (str(len(get_all_singer_pages)), str(num)))
            num += 1
    except Exception as msg:
        traceback.print_exc()

def main():

    # 获取所有歌手类型
    # get_singers_pages_url()

    # 获取所有歌手专辑页面
    # get_all_singer_user_page()

    with open('txt', 'r') as f:
        con = f.readlines()

    ss = str(con).split('-')
    print(len(ss))

if __name__ == '__main__':
    myTool = ip_tool.ResponseTool()
    headers, proxies = myTool.headers, myTool.proxies

    url = 'https://music.163.com'

    # 抓取歌手的页面
    get_all_singer_pages = list()


    main()
