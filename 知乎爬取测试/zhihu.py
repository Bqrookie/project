# -*- coding: utf-8 -*-
import requests
import json
import re
from bs4 import BeautifulSoup
import ResponseTool as myTool


def main():

    id = 55491488
    offer = 0
    sort_by = 'default'
    '''
    sort_by=default 默认排序
    sort_by=updated 时间排序
    '''

    for i in range(999):
        url = "https://www.zhihu.com/api/v4/questions/" + str(id) + "/answers?include=data[*].\
is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail\
%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content\
%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2\
Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2\
Cis_labeled%2Cis_recognized%2Cpaid_info%3Bdata[*].mark_infos[*].url%3Bdata[*].author.follower_count%2Cbadge[*]\
.topics&limit=20&offset=" + str(offer) + "&platform=desktop&sort_by=" + sort_by

        print('正在爬取第%s页' % (str(i+1),))
        do_work(url)
        offer += 20
        print(' ')


def do_work(url):
    to = myTool.ResponseTool()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    req = requests.get(
        url,
        proxies={"http": to.proxies}, headers=headers)
    if req.status_code == 200:
        try:
            result = json.loads(req.text)
            if result['data']:
                num = len(result['data'])


                for j in range(num):
                    res = result['data'][j]
                    person = "https://www.zhihu.com/people/" + str(res['author']['url_token']) + "/activities"

                    if res['author']['id'] == '0':

                        print('[用户名]【%s】' % (res['author']['name'],))
                        print('[个人主页]【%s】' % ('no_type',))
                        print('[个性签名]【%s】' % ('no_type',))
                        print('[粉丝数]【%s】' % ('no_type',))
                        print('[点赞数]【%s】' % (res['voteup_count'],))
                        print('[评论数]【%s】' % (res['comment_count'],))
                        jg = res['content'].replace("<noscript>", "<!--<noscript>").replace("</noscript>",
                                                                                            "</noscript>-->")
                        aaa = re.sub(r'<\!\-\-.*?\-\->', "", jg)
                        bbb = re.sub('<p class="ztext-empty-paragraph">(.+?)</p>', '', aaa)
                        # print('[内容]【%s】' % (bbb), )

                        # print('[内容]【%s】' % (bbb), )
                        if '<figure' in bbb:
                            result = work(bbb)
                            while True:
                                if '<figure' in result:
                                    result = work(result)
                                else:
                                    print(result)
                                    break
                            # soup = BeautifulSoup(bbb, 'html.parser')
                            # rrr = soup.find_all('figure')
                            # for i in range(len(rrr)):
                            #     print(rrr[i])

                    else:
                        print('[用户名]【%s】' % (res['author']['name'],))
                        print('[个人主页]【%s】' % (person,))
                        print('[个性签名]【%s】' % (res['author']['headline'] if res['author']['headline'] else 'no_type',))
                        print('[粉丝数]【%s】' % (res['author']['follower_count'],))
                        print('[点赞数]【%s】' % (res['voteup_count'],))
                        print('[评论数]【%s】' % (res['comment_count'],))
                        jg = res['content'].replace("<noscript>", "<!--<noscript>").replace("</noscript>",
                                                                                            "</noscript>-->")
                        aaa = re.sub(r'<\!\-\-.*?\-\->', "", jg)
                        bbb = re.sub('<p class="ztext-empty-paragraph">(.+?)</p>','', aaa)
                        # print('[内容]【%s】' % (bbb), )
                        if '<figure' in bbb:
                            result = work(bbb)
                            while True:
                                if '<figure' in result:
                                    result = work(result)
                                else:
                                    print(result)
                                    break
                            # soup = BeautifulSoup(bbb, 'html.parser')
                            # rrr = soup.find_all('figure')
                            # for i in range(len(rrr)):
                            #     print(rrr[i])

                    if j == 2:
                       print("没有了")
                       exit(1)
                    print(' ')
            else:
                print("没有了")
                print('总共%s条数据 ' % (str(json.loads(req.text)['paging']['totals'])))
                exit(1)
        except Exception as msg:
            print(msg)

def work(sss):
    head_num = sss.find('<figure')
    head_str = sss[:head_num]
    sea_str = sss[head_num:]
    jq_num = sea_str.find('</figure>')
    re_str = sea_str[:jq_num+9]
    jq = len(re_str)

    resu = re_str.find('data-original') + 15

    res = re_str[resu:].split('"')[0]
    zui_hou_yi_ji = '<img src="' + res + '" alt="pic ！！！">'

    return head_str+ zui_hou_yi_ji +sss[head_num+jq:]


if __name__ == "__main__":
    main()
