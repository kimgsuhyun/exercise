#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://foodnara.go.kr/kisna/index.do?nMenuCode=17&page=4&mPart=&code2=&code4=1&search_name=&processed=&order_column=2&order_asc=asc").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")


readNum_1=[]
father=soup.select('.tableGray > tbody > tr')
for rea in father:
	readNum_1.append(rea.get_text())
print readNum_1[1].encode("utf-8")
