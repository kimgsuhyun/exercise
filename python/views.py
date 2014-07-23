from flask import render_template, Flask
from apps import app
import urllib2
import urllib
from bs4 import BeautifulSoup





@app.route('/')
@app.route('/index')
def index():
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
			for j in self.spli:
				self.player.append(j)
			
			return self.player
	age = 24;
	name = 'suhyun kim'
	likelion = ['student', 'teacher', 'computer']

	# b=base("http://kbodata.news.naver.com/m_rank/rank_batter.asp",".table_board2 > tbody > tr")
	# base2=b.run(4)
	b=base("http://kbodata.news.naver.com/m_rank/rank_batter.asp",".table_board2 > tbody > tr")
	data = zip(b.run(0),b.run(5))


	return render_template("index.html", data=data)


#mj
# def index():
#    htmltext = urllib.urlopen("http://likelion.fiv3star.me/index.php?mid=board_MzBS61").read()

#    soup = BeautifulSoup(htmltext, from_encoding="utf-8")

#    authors = []

# # assignment one.b

#    for tag in soup.select("td.title"):
#       authors.append(tag.get_text())

#    # for author in authors:
#    #    print author.encode('utf-8')

#    return render_template("index.html" , items=authors)