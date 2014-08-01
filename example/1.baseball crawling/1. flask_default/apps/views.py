from flask import render_template, Flask
from apps import app
import urllib2
import urllib
from bs4 import BeautifulSoup
class base :
	def __init__(self,url,route):
		self.url=url
		self.f = urllib2.urlopen(self.url)
		self.page = self.f.read().decode('cp949', 'ignore')
		self.f.close()
		self.soup = BeautifulSoup(self.page)
		self.a = self.soup.select(route)
		#if contents is blank,must do removing!!!!!
	def run(self,rank):
		self.player=[]
		self.spli=self.a[rank].get_text()
		for j in self.spli.split('\n'):
			if j!=" ":
				self.player.append(j)
		return self.player[2:]
@app.route('/')
@app.route('/index')
def index():

	age = 24;
	name = 'suhyun kim'
	likelion = ['student', 'teacher', 'computer']


	b=base("http://kbodata.news.naver.com/m_rank/rank_batter.asp",".table_board2 > tbody > tr")
	data = []
	for i in range(49):
		data.append(b.run(i))

	return render_template("index.html", data=data)

