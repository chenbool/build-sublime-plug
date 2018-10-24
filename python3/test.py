# -*- coding:utf-8 -*
#__author__ = 'bool'

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from time import strftime,time
from Plug import Plug

class Api(object):

	def __init__(self):
		pass
		
	def getContent(self, url):
		resp = urlopen(url).read().decode("utf-8")
		soup = bs(resp,"html.parser")
		return soup

	# yaf 手册
	def yaf(self):
		soup = self.getContent("http://php.net/manual/zh/book.yaf.php")
		listRes = soup.find("div", {"class": "book"}).find("ul", {"class": "chunklist chunklist_book"})
		liRes = listRes.findAll('li')

		del liRes[0:9]

		for v in liRes:
			temp = v.findAll('li')

			for x in temp:
				desc = x.get_text().split('—')
				dirName = desc[0].split('::')[0].lower()
				print( desc )
				plug = Plug('C:/Users/Administrator/Desktop/y/',dirName+'/')
				plug.build(desc[0].strip(),desc[0].strip(),desc[1].strip(),'source.php')
	

	# swoole 手册
	def swoole(self):
		soup = self.getContent("http://php.net/manual/zh/book.swoole.php")
		listRes = soup.find("div", {"class": "book"}).find("ul", {"class": "chunklist chunklist_book"})
		liRes = listRes.findAll('li')

		del liRes[0:7]

		for v in liRes:
			temp = v.findAll('li')
			# print(temp[0])
			for x in temp:
				desc = x.get_text().split('—')
				dirName = desc[0].split('::')[0].lower()
				print( desc )
				plug = Plug('C:/Users/Administrator/Desktop/sublime_swoole/',dirName+'/')
				plug.build(desc[0].strip(),desc[0].strip(),desc[1].strip(),'source.php')


	# swoole const预定义常量
	def const(self):
		soup = self.getContent("http://php.net/manual/zh/swoole.constants.php")
		dlRes = soup.find("div", {"class": "appendix"}).find("dl")
		dtRes = dlRes.findAll('dt')

		for v in dtRes:
			name =  v.find('strong').get_text()
			types =  v.find('span').find('a').get_text()
			print( name )
			print( types )
			plug = Plug('C:/Users/Administrator/Desktop/constants/','/')
			plug.build(name,name,types,'source.php')

		# exit()	
		

if __name__ == '__main__':
	api = Api()
	api.const()