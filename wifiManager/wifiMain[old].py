# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import db_sql as db


res_data = db.get_data()
window = tk.Tk()
window.title('wifi manager')
window.geometry('860x470')
# 阻止Python GUI的大小调整
window.resizable(0, 0)
# window.overrideredirect(True)
window.iconbitmap('C:/Users/Administrator/Desktop/Git/wifiManager/ico.ico')
# 窗口透明度60 %
window.attributes("-alpha", 0.9)


def window_quit():
    window.destroy()

def dojob():
    # print(res_data)
    data = list()
    for i in res_data:
        data.append(i)
    # print('ok')


def insert():
    pass

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Add', command=insert)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window_quit)

frm = tk.Frame(window)
frm_t = tk.Frame(frm)
frm_b = tk.Frame(frm, height=30)


tree = ttk.Treeview(frm_t, columns=[
                    '1', '2', '3', '4', '5', '6', '7', '8'], height=20, show="headings")
tree_width = [23, 130, 180, 150, 100, 100, 70, 100]
tree_option = ['id', 'mac', 'ssid', 'pwd',
               'router', 'routerPwd', 'pin', 'remark']
for row in range(1, 9):
    tree.column(str(row), width=tree_width[row - 1], anchor='center')

for row in range(1, 9):
    tree.heading(str(row), text=tree_option[row - 1])


for row in res_data:
    tree.insert('', 'end', values=row)
tree.pack(side='left')
# "id mac router routerPwd pin pwd ssid remark"

tk.Label(frm_b, text='作者:testpython').pack()

frm_t.pack(side='top')
frm_b.pack(side='bottom')
frm.pack()


def treeviewDoubleClick(event):
    varstr = list()
    for item in tree.selection():
        item_text = tree.item(item, "values")
        for row in item_text:
            varstr.append(row)
    try:
        varstr[2]
    except IndexError as e:
        tk.messagebox.showerror(title='注意', message='请选择正确的值')
        return

    win = tk.Toplevel(window)
    win.geometry('250x300')
    win.title(varstr[2])
    # 阻止Python GUI的大小调整
    win.resizable(0, 0)
    win.iconbitmap('C:/Users/Administrator/Desktop/Git/wifiManager/ico.ico')
    # 窗口透明度60 %
    win.attributes("-alpha", 0.9)

    def callback():
        for item in tree.get_children():
            tree.delete(item)

        res_data = db.get_data()
        win.destroy()

        for row in res_data:
            tree.insert('', 'end', values=row)

    win.protocol("WM_DELETE_WINDOW", callback)

    win_frm = tk.Frame(win)

    name_list = ['id', 'mac', 'ssid', 'pwd',
                 'router', 'routerPwd', 'pin', 'remark']
    for set_len in name_list:
        set_len += '\t'

    for set_value in range(8):

        name = 'L' + str(set_value)
        name = tk.Label(win_frm, text=name_list[set_value], justify='left')
        name.grid(row=set_value, column=0)

        name_list[set_value] = tk.Text(win_frm, height=1, width=20)
        name_list[set_value].insert('insert', varstr[set_value])
        name_list[set_value].grid(row=set_value, column=1)

    edit_btn = tk.Button(win_frm, text='Edit')
    edit_btn.grid(row=9, column=0)

    del_btn = tk.Button(win_frm, text='Del')
    del_btn.grid(row=9, column=1)

    exit_btn = tk.Button(win_frm, text='Exit', command=callback)
    exit_btn.grid(row=9, column=2)
    win_frm.grid()

# tree.bind('<ButtonRelease-1>', treeviewClick)  # 绑定单击离开事件===========
tree.bind('<Double-1>', treeviewDoubleClick)  # 绑定单击离开事件===========

window.config(menu=menubar)
window.mainloop()
