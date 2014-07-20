#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import csv

htmltext = urllib.urlopen("http://foodnara.go.kr/kisna/index.do?nMenuCode=17&page=2&mPart=&code2=&code4=2&search_name=&processed=&order_column=2&order_asc=asc").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")


readNum_1=[]

father=soup.select('.tableGray > tbody > tr')

for rea in father:
	readNum_1.append(rea.get_text())
a=readNum_1[3].encode("utf-8")
d=str.split(a)
print d[3].encode("utf-8")
