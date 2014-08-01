import smtplib
import urllib2
from bs4 import BeautifulSoup

# url="http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1="



# url=url+"105"
# f = urllib2.urlopen(url)
# page = f.read().decode('cp949', 'ignore')
# f.close()

# soup = BeautifulSoup(page)

# result=""


# for each in soup.select(".type02_headline > li"):
# 	result += each.a.string +'\n'

# print result.encode('utf-8')
	
	


def news_s(num):
	f = urllib2.urlopen("http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1="+str(num))
	page = f.read().decode('cp949', 'ignore')
	f.close()
	soup = BeautifulSoup(page)
	result=""
	for each in soup.select(".type02_headline > li"):
		result += each.a.string +'\n'
	return result

news="what"	
U=0	
	

news=news_s(105)
print news[4].encode('utf-8')