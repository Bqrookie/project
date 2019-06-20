import ip_tool
import csv
import requests
import json
import queue
import threading
import time

# 创建一个队列
page_queue = queue.Queue(50)
# 创建一个线程锁，防止多线程写入文件时发生错乱
mutex_lock = threading.Lock()

out = open('bili.csv', 'a+', newline='')
csv_write = csv.writer(out, dialect='excel')
title_list = ['标题', '播放次数', '评论人数', '时长', '收藏人数', '发布时间', '视频截图', '视频播放地址']
csv_write.writerow(title_list)


def get_user_pages(user_id):
    """
    获取所有页面链接
    :return:
    """
    # 最大页面
    max_pages = 0
    tmp_url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=%s&pagesize=30&tid=0&page=1&keyword=&order=\
    pubdate" % str(user_id)
    proxies, headers = get_proxies_headers()
    # 使用try、except来捕获异常
    # 如果不捕获异常，程序可能崩溃
    try:
        # 使用代理访问
        req = requests.get(tmp_url, proxies={"http": proxies}, timeout=5, headers=headers)
        # 没有报异常，说明访问成功
        # 获得返回数据
        if req.status_code == 200:
            max_pages = json.loads(req.text)['data']['pages']
        else:
            raise Exception
    except Exception as msg:
        # 访问失败 打印错误信息
        print("fun:get_user_pages【%s】" % (msg,))

    return max_pages


def get_proxies_headers():
    """
    获取随机的ip和header
    :return:
    """
    proxies = ip_tool.get_proxies()
    # 获取一个随机user_agent
    headers = ip_tool.get_headers()

    return proxies, headers


def get_video():
    video_list = list()
    while not page_queue.empty():
        try:
            this_page = page_queue.get()
            proxies, headers = get_proxies_headers()
            # 使用try、except来捕获异常
            # 如果不捕获异常，程序可能崩溃
            # 使用代理访问
            req = requests.get(this_page, proxies={"http": proxies}, timeout=5, headers=headers)
            # 没有报异常，说明访问成功
            # 获得返回数据
            if req.status_code == 200:
                video_list.append(json.loads(req.text)['data']['vlist'])
                for item in json.loads(req.text)['data']['vlist']:
                    # 评论人数 时长 发布时间 标题 播放次数视频截图 视频播放地址 收藏人数
                    #  评论人数
                    comment = item['comment']
                    # 时长
                    length = item['length']
                    # 发布时间
                    timeArray = time.localtime(item['created'])
                    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    created = otherStyleTime
                    # 标题
                    title = item['title']
                    # 播放次数
                    play = item['play']
                    # 视频截图
                    pic = item['pic']
                    # 视频播放地址
                    aid = 'https://www.bilibili.com/video/av%s' % item['aid']
                    # 收藏人数
                    favorites = item['favorites']

                    result_list = [title, play, comment, length, favorites, created, pic, aid]
                    # 申请获取锁，此过程为阻塞等待状态，直到获取锁完毕
                    mutex_lock.acquire()
                    # 追加数据写入csv文件，若文件不存在则自动创建
                    csv_write.writerow(result_list)
                    print('[%s采集完成]' % (item['aid'],))
                    # 释放锁
                    mutex_lock.release()
            else:
                raise Exception
        except Exception as msg:
            print('fun:get_video【%s】' % (msg,))


def main():

    # user_id = int(input('ID:'))
    # thread_num = int(input('Thread:'))
    thread_num = 50  # 测试线程数，可以根据自己情况更改
    user_id = 28152409  # 测试账号ID

    # 获取所有页面链接
    max_pages = get_user_pages(user_id)

    # 把需要采集的页面放到队列里面
    for item in range(1, max_pages+1):
        item_url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=%s&pagesize=30&tid=0&page=%s&keyword=&order=pubdate" % (str(user_id), str(item))
        page_queue.put(item_url)

    # 线程数为50，在一定范围内，线程数越多，速度越快
    for i in range(thread_num):
        t = threading.Thread(target=get_video)
        t.start()


if __name__ == '__main__':
    main()
