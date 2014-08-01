# import urllib2
# from bs4 import BeautifulSoup
# import csv

# def basecraw(url,clas,i):
# 	f = urllib2.urlopen(url)
# 	page = f.read().decode('cp949', 'ignore')
# 	f.close()

# 	soup = BeautifulSoup(page)
# 	a = soup.select(clas)
# 	b=a[i].text.encode("utf-8")
# 	c=b.replace(" ","")
# 	return c

# print basecraw("http://kbodata.news.naver.com/m_rank/rank_batter.asp",'.table_board2 > tbody > tr > td',0)
abc=['a','b','c']
ccc=[1,2,3]
for i in abc:
	for j in ccc:
		i,j
		print i,j


