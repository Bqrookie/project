# -*- coding:utf-8 -*-

import db_sql as db
import urllib
import os

mode="mode con: cols=150 lines=40"#最关键的
color="color 72"#最关键的
os.system(mode)#最关键的
os.system(color)#最关键的
print(u"论坛审核提示程序--依山居\n")

def main():
    res_data = db.get_data()

    from prettytable import PrettyTable

    a = PrettyTable(['id', 'mac', 'ssid', 'pwd'])
     
    a.align["姓名"] = "1" #以姓名字段左对齐
    a.padding_width = 4  # 填充宽度
    for num in range(len(res_data)):
        # print(res_data[num])

        aa = res_data[num].split(' ')[0]
        bb = res_data[num].split(' ')[1]
        cc = res_data[num].split(' ')[2]
        dd = res_data[num].split(' ')[3]
        a.add_row([aa,bb, cc, dd])

    print(a)
    input()

# print('a')

if __name__ == '__main__':
    main()
