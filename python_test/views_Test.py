import urllib2
import urllib
from bs4 import BeautifulSoup
from flask import render_template, Flask


class base :
	def __init__(self,url,route):
		self.url=url
		self.f = urllib2.urlopen(self.url)
		self.page = self.f.read().decode('cp949', 'ignore')
		self.f.close()
		self.soup = BeautifulSoup(self.page)
		self.a = self.soup.select(route)
	def run(self,rank):
		self.player=[]
		self.spli=self.a[rank].get_text()
		for j in self.spli.split('\n'):
			self.player.append(j)
		return self.player[2:]


age = 24;
name = 'suhyun kim'
likelion = ['student', 'teacher', 'computer']






	# zip?!?!
# b=base("http://kbodata.news.naver.com/m_rank/rank_batter.asp",".table_board2 > tbody > tr")
# # print b.run(0)[1].encode("utf-8")
# data = zip(b.run(0),b.run(5))
# print data
# # for row in data:
# 	for cell in row:
# 		print cell,
# print b.a


# 	another way
# f = urllib2.urlopen("http://kbodata.news.naver.com/m_rank/rank_batter.asp")
# page = f.read().decode('cp949', 'ignore')
# f.close()
# soup = BeautifulSoup(page)
# result=""
# for each in soup.select(".table_board2 > tbody > tr"):
# 	result += each.td

# print result

	# double list , list in list. 
b=base("http://kbodata.news.naver.com/m_rank/rank_batter.asp",".table_board2 > tbody > tr")
print b.run(0)
basee=[]
for i in range(3):
	basee.append(b.run(i))
base2=basee
print base2


