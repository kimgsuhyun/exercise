#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import urllib2

url = "http://foodnara.go.kr/kisna/index.do?nMenuCode=17&page=2&mPart=&code2=&code4=2&search_name=&processed=&order_column=2&order_asc=asc"
f = urllib2.urlopen(url)
page = f.read().decode('cp949', 'ignore')
f.close()

soup = BeautifulSoup(page)


readNum_1=[]
father=soup.select('.tableGray > tbody > tr')

for rea in father:
	readNum_1.append(rea.get_text())
a=readNum_1[3]
print str.split(a)




