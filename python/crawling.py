import urllib2
from bs4 import BeautifulSoup
import sys

url = "http://foodnara.go.kr/kisna/index.do?nMenuCode=17&page=2&mPart=&code2=&code4=2&search_name=&processed=&order_column=2&order_asc=asc"
f = urllib2.urlopen(url)
page = f.read().decode('cp949', 'ignore')
f.close()

soup = BeautifulSoup(page)
a = soup.select('.tableGray > tbody > tr')
# print a


b=a[0].get_text()
d=b.replace("	",'')

c=d.split('\n')


# print c[2].encode('utf-8')+","+c[4].encode('utf-8')+","+c[7].encode('utf-8')+c[10].encode('utf-8')


for i in range(100):
	print c[i].encode('utf-8'),




# for i in range(49):
	# print a[i].text.encode("utf-8")
# for i in range(8):
#    img = a[i].text
#    print img.encode("utf-8")
