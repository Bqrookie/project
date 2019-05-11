# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import db_sql as db


def main():
	# res_data = db.get_data()
	pass

global win
res_data = db.get_data()
image = None
im = None

# 窗口设置
window = tk.Tk()
window.title('管理器')
window.geometry('860x470')
# 阻止Python GUI的大小调整
window.resizable(0, 0)
# window.overrideredirect(True)
window.iconbitmap('C:/Users/Administrator/Desktop/Git/wifiManager/images/ico.ico')
# 窗口透明度60 %
# window.attributes("-alpha", 0.9)


# 菜单栏
menubar = tk.Menu(window)

# file_menu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='文件', menu=file_menu)
#
# set_menu = tk.Menu(menubar, tearoff=0)
# # menubar.add_cascade(label='Home', menu=filemenu)
# menubar.add_cascade(label='选项', menu=set_menu)

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='选项', menu=help_menu)
help_menu.add_command(label='关于')
help_menu.add_command(label='技术支持')
help_menu.add_command(label='在线更新')


tabControl = ttk.Notebook(window)          # Create Tab Control

tab_home = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab_home, text='首页')      # Add the tab
tab_manager = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab_manager, text='管理')      # Make second tab visible
tab_find = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab_find, text='发现')      # Make second tab visible
tabControl.pack(expand=1, fill="both")  # Pack to make visible

# Home 图片
canvas = tk.Canvas(tab_home, height=700, width=700)
image_file = tk.PhotoImage(file='images/Home.gif')
image = canvas.create_image(340,210, anchor='center', image=image_file)
canvas.pack()

# 管理页面数据展示
cloumns_list = ['1','2','3', '4', '5', '6', '7', '8']
heading_list = ['id', 'mac', 'ssid', 'pwd', 'router', 'routerPwd', 'pin', 'remarks']

tree = ttk.Treeview(tab_manager,columns=cloumns_list, show='headings')

for	temp in range(len(heading_list)):
	tree.column(str(temp+1), width=107, anchor='center')

for	temp in range(len(heading_list)):
	tree.heading(str(temp+1),text=heading_list[temp])

for temp in res_data:
	tree.insert('', 'end', values=temp.split(' '))
tree.pack(side='left', fill='both')


def treeviewClick(event):  # 单击
	for item in tree.selection():
		item_text = tree.item(item, "values")
		pass

	li = tree.item(tree.selection())['values']
	top_tk(li)



def top_tk(li):
	edit = {}
	global win
	global name_text
	try:
		win.destroy()
	except Exception as ret:
		print('debug:[%s]' % ret)
	finally:
		win = tk.Toplevel(window)
		win.geometry('250x300')
		win.title(str(li[2]))
		# 阻止Python GUI的大小调整
		win.resizable(0, 0)
		win.iconbitmap('C:/Users/Administrator/Desktop/Git/wifiManager/images/ico.ico')
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

		def edit_data():

			da = dict()
			da['mac'] = name_mac.get()
			da['router'] = name_router.get()
			da['routerPwd'] = name_routerPwd.get()
			da['pin'] = name_pin.get()
			da['pwd'] = name_pwd.get()
			da['ssid'] = name_ssid.get()
			da['remarks'] = name_remarks.get()
			try:
				db.edit_data(da, li[0])
			except Exception as ret:
				print(ret)
			finally:
				callback()

		def del_data():

			try:
				db.del_data(li[0])
			except Exception as ret:
				print(ret)
			finally:
				callback()

		def add_data():
			add = dict()
			add['mac'] = name_mac.get()
			add['router'] = name_router.get()
			add['routerPwd'] = name_routerPwd.get()
			add['pin'] = name_pin.get()
			add['pwd'] = name_pwd.get()
			add['ssid'] = name_ssid.get()
			add['remarks'] = name_remarks.get()

			try:
				db.insert_data(add)
			except Exception as ret:
				print(ret)
			finally:
				callback()

		L1 = tk.Label(win, text='mac', justify='left')
		L1.grid(row=0, column=0)

		L2 = tk.Label(win, text='ssid', justify='left')
		L2.grid(row=1, column=0)

		L3 = tk.Label(win, text='pwd', justify='left')
		L3.grid(row=2, column=0)

		L4 = tk.Label(win, text='router', justify='left')
		L4.grid(row=3, column=0)

		L5 = tk.Label(win, text='routerPwd', justify='left')
		L5.grid(row=4, column=0)

		L6 = tk.Label(win, text='pin', justify='left')
		L6.grid(row=5, column=0)

		L7 = tk.Label(win, text='remarks', justify='left')
		L7.grid(row=6, column=0)

		name_mac = tk.Entry(win)
		name_mac.insert('insert', li[1])
		name_mac.grid(row=0, column=1)

		name_ssid = tk.Entry(win)
		name_ssid.insert('insert', li[2])
		name_ssid.grid(row=1, column=1)

		name_pwd = tk.Entry(win)
		name_pwd.insert('insert', li[3])
		name_pwd.grid(row=2, column=1)

		name_router = tk.Entry(win)
		name_router.insert('insert', li[4])
		name_router.grid(row=3, column=1)

		name_routerPwd = tk.Entry(win)
		name_routerPwd.insert('insert', li[5])
		name_routerPwd.grid(row=4, column=1)

		name_pin = tk.Entry(win)
		name_pin.insert('insert', li[6])
		name_pin.grid(row=5, column=1)

		name_remarks = tk.Entry(win)
		name_remarks.insert('insert', li[7])
		name_remarks.grid(row=6, column=1)

		edit_btn = tk.Button(win, text='Edit', width=20, command=edit_data)
		edit_btn.grid(row=9, column=1)

		exit_btn = tk.Button(win, text='Exit',  width=20, command=callback)
		exit_btn.grid(row=10, column=1)

		del_btn = tk.Button(win, text='Del', width=20, command=del_data)
		del_btn.grid(row=11, column=1)

		del_btn = tk.Button(win, text='Add', width=20, command=add_data)
		del_btn.grid(row=12, column=1)

		win.mainloop()


tree.bind('<Double-Button-1>', treeviewClick)  # 绑定单击离开事件===========

window.config(menu=menubar)
window.mainloop()

if __name__ == '__main__':
	main()
