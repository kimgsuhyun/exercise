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




# print c[2].encode('utf-8')+","+c[4].encode('utf-8')+","+c[7].encode('utf-8')+c[10].encode('utf-8')


# for i in range(100):
# 	print c[i].encode('utf-8'),

# print a
b=a[2].get_text()
c=d.split('\n')

# for i in c:

#    # print c.index(i)

#    print i.encode('utf-8')
nutrition={}
c[56].encode('utf-8')+c[66].encode('utf-8')+c[76].encode('utf-8')+c[86].encode('utf-8')+c[96].encode('utf-8')

nutrition['numb'] = c[2].encode('utf-8')
nutrition['type'] = c[4].encode('utf-8')
nutrition['menu'] = c[7].encode('utf-8')
nutrition['provide'] = c[9].encode('utf-8')
nutrition['kcal'] = c[16].encode('utf-8')
nutrition['carbo'] = c[26].encode('utf-8')
nutrition['protein'] = c[36].encode('utf-8')
nutrition['fat'] = c[46].encode('utf-8')
nutrition['sugar'] = c[56].encode('utf-8')
nutrition['na'] = c[66].encode('utf-8')
nutrition['choles'] = c[76].encode('utf-8')
nutrition['saturate'] = c[86].encode('utf-8')
nutrition['trans'] = c[96].encode('utf-8')

print nutrition['trans']