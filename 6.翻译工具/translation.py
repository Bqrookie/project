import requests
import ResponseTool as my_tool
import google_tk as g_tk
import json


class Translation:

	def __init__(self, query, flag=False):
		"""
		默认就是中文翻译成英文
		:param query: 翻译的文字
		:param flag: False就是中译英 True就是英译中
		"""
		# 默认就是中文=>英文
		self.flag = flag
		self.query = query

	def do_tran(self):

		res_tool = my_tool.ResponseTool()

		if not self.flag:
			local_url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=\
bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=2&ssel=3&tsel=3&kc=1&tk=%s&\
q=%s' % (str(g_tk.Py4Js().getTk(self.query)), res_tool.url_conversion(self.query, True))
		else:
			local_url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=\
at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=3&tsel=0&kc=1&tk=%s&\
q=%s' % (str(g_tk.Py4Js().getTk(self.query)), res_tool.url_conversion(self.query))


		# 使用try、except来捕获异常
		# 如果不捕获异常，程序可能崩溃
		try:
			# 使用代理访问
			req = requests.get(local_url, proxies={"http": res_tool.get_proxies()}, timeout=5, headers=res_tool.get_headers())

			if req.status_code == 200:
				a = json.loads(req.text)
				for item in a:
					print(item)
			else:
				# 访问异常直接抛出
				raise Exception
		except Exception as msg:
			print(req.status_code)
			print("fun:tran【%s】" % (msg,))


if __name__ == '__main__':
	test_var = Translation('北京')
	test_var.do_tran()
