import os
from tkinter import *
import psutil
from tkinter import messagebox

root = Tk()                     # 创建窗口对象的背景色
root.title("微信多开")

# 设置窗口的大小
root.geometry("230x145")
root.maxsize(230, 195)  
root.minsize(230, 195)

path_list = ['C:/Program Files (x86)/Tencent/WeChat/', 'D:/Program Files (x86)/Tencent/WeChat/']

path = ''


def do_work():
    try:
        # 先判断目录是否存在
        for file_path in path_list:
            if os.path.exists(file_path):
                path = file_path
                break
            else:
                messagebox.showerror('Error', '请确保微信安装在【C/D】默认路径')
                raise ValueError
        # 目录存在就切换路径
        os.chdir(path)

        # 运行微信之前先关闭所有微信进程
        close_vx()

        # 运行微信程序
        str_cmd = 'start WeChat.exe'
        for x in range(1,6):
            os.system(str_cmd)
    except Exception as e:
            print(e)
    finally:
        print('程序已经结束')


def close_vx():
    try:

        proc_name = "WeChat.exe"
        pids = psutil.pids()
        for each_pid in pids:
            p = psutil.Process(each_pid)
            if p.name() == proc_name:
                p.terminate()
    except Exception as e:
            print(e)
    finally:
        print('程序已经结束')


# 通过command属性来指定Button的回调函数
Button(root, text='一键微信多开', width=32,height=5, command=do_work).pack()
Button(root, text='关闭所有微信', width=32,height=5, command=close_vx).pack()

root.mainloop()  # 进入消息循环
