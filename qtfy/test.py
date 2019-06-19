import re
import requests
import ip_tool
import time
import random


def main():

    url = 'https://www.xicidaili.com/nn/9'
    headers =ip_tool.get_headers()
    proxies = ip_tool.get_proxy()
    r = requests.get(url, headers=headers, proxies=proxies)

    if r.status_code == 200:
        re_td = r'<td>(.*)</td>'
        a, b = 0, 1
        result_list = list()
        pattern1 = re.compile(re_td)
        res = pattern1.findall(r.text)
        if res:
            result_list.append(res)

        for i in range(100):
            try:
                print("%s:%s" % (str(result_list[0][a]), str(result_list[0][b])))
                a += 5
                b += 5
            except Exception as e:
                print(e)

def get_id():
    shop_list = ['https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w137644-21730831590.32.3e5f67a65SwK4V&id=595359676040',
                 'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21730831595.4.3e5f67a65SwK4V&id=597005755282',
                 'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21730831595.18.3e5f67a65SwK4V&id=596740966951',
                 'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21730831595.26.3e5f67a65SwK4V&id=595903427157',
                 'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w137644-21730831590.41.3e5f67a6zoMpgB&id=595358444871',
                 'https://item.taobao.com/item.htm?id=596740966951',

                 ]
    return random.choice(shop_list)
def test():
    headers = ip_tool.get_headers()
    proxies = get_proxies()
    i=1
    while True:
        time.sleep(2)
        print('第%s次' % (str(i),), end='')
        try:
            r = requests.get(get_id(), headers=headers, proxies={'http':proxies}, timeout=5)
            if r.status_code == 200:
                print('正常访问')
        except Exception as e:
            print('error:[%s]' % (proxies,))
            proxies = get_proxies()
        finally:
            i += 1


def get_proxies():
    proxies = ip_tool.get_proxies()
    return proxies
if __name__ == '__main__':
    # main()
    test()
