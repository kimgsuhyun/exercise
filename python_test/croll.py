import urllib2
from bs4 import BeautifulSoup


htmltext = urllib2.urlopen("http://foodnara.go.kr/kisna/index.do?nMenuCode=17&code4=2").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

a = soup.select('.tableGray > tbody > tr')
print a
crawl=a[0].get_text()

crawl_li=str.split(crawl.encode('utf-8'))