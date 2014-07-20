import urllib2
from bs4 import BeautifulSoup

url = "http://kbodata.news.naver.com/m_rank/rank_team.asp"
f = urllib2.urlopen(url)
page = f.read().decode('cp949', 'ignore')
f.close()

soup = BeautifulSoup(page)
a = soup.findAll('td', attrs={'class': 'left padd '})
print a
for i in range(8):
   img = a[i].text
   print img.encode("utf-8")