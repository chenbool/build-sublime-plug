# -*- coding: utf-8 -*-

import re
from os import path,makedirs
from time import time

class Plug(object):
	def __init__(self,root_path, base_path='/'):
		self.root_path = root_path
		self.base_path = base_path
	
	def build(self,trigger,content,desc,scope='source.php'):
		tpl = '''<snippet>
	<content><![CDATA[%s]]></content>
	<scope>%s</scope>
	<tabTrigger>%s</tabTrigger>
	<description>%s</description>
</snippet>
		''' % (content,scope,trigger,desc)

		filename = re.sub(':','',trigger.strip() ).replace('\\','')
		# filename = re.sub('[\\/:]','',trigger.strip() )
		base_path = self.root_path + self.base_path
		filepath = base_path + filename + str( int(time()) ) + '.sublime-snippet'

		# 检测目录是否存在
		if not path.exists(base_path):
			makedirs(base_path)
		f = open(filepath, 'w')
		f.write(tpl)
		f.close()

if __name__ == '__main__':
  plug = Plug()
  # plug.build('where','where(...)','where条件','source.py')
