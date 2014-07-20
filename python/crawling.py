import urllib2
from bs4 import BeautifulSoup

url = "http://foodnara.go.kr/kisna/index.do?nMenuCode=17&page=2&mPart=&code2=&code4=2&search_name=&processed=&order_column=2&order_asc=asc"
f = urllib2.urlopen(url)
page = f.read().decode('cp949', 'ignore')
f.close()

soup = BeautifulSoup(page)
a = soup.select('.tableGray > tbody > tr')
# print a
b=a[0].get_text()
c=b.encode("utf-8")
print c

# for i in range(8):
#    img = a[i].text
#    print img.encode("utf-8")

