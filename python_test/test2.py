import urllib
from bs4 import BeautifulSoup
import smtplib
import time

htmltext = urllib.urlopen("http://likelion.fiv3star.me/index.php?mid=board_MzBS61").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")
title_1=[]
author_1=[]
time_1=[]
readNum_1=[]
total=[title_1,author_1,time_1,readNum_1]
for ti in soup.select(".title"):
	title_1.append(ti.get_text())
for au in soup.select(".author"):
	author_1.append(au.get_text())
for rea in soup.select(".no"):
	readNum_1.append(rea.get_text())
for tim in soup.select(".time"):
	time_1.append(tim.get_text())
print total[0][1].encode("utf-8"),total[1][0].encode("utf-8"),total[2][1],total[3][0]

readNum_1=[]

for rea in soup.select(".no"):
	readNum_1.append(rea.get_text())
print readNum_1
# to = 'gamiduka@gmail.com'
# gmail_user = 'tonyoh.fiv3star'
# gmail_pwd = 'likelion'
# smtpserver = smtplib.SMTP("smtp.gmail.com",587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo
# smtpserver.login(gmail_user, gmail_pwd)
# header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
# print header

# for i in title_1:
# 	ii=str(i.encode("utf-8"))
# 	for n in str.split(ii):
# 		if n=="suhyun":
# 			msg = header + '\n this is test msg from mkyong.com \n\n'
# 			smtpserver.sendmail(gmail_user, to, msg)
# 			print 'done!'
# 		else:
# 			print "none"


# smtpserver.close()
c=0
nu2=readNum_1
while c==0:
	htmltext = urllib.urlopen("http://likelion.fiv3star.me/index.php?mid=board_MzBS61").read()
	soup = BeautifulSoup(htmltext, from_encoding="utf-8")
	readNum_1=[]
	for rea in soup.select(".no"):
		readNum_1.append(rea.get_text())
	if nu2==readNum_1:
		print "waiting"
		time.sleep(5)
	else:
		title_1=[]
		author_1=[]
		time_1=[]
		readNum_1=[]
		total=[title_1,author_1,time_1,readNum_1]
		for ti in soup.select(".title"):
			title_1.append(ti.get_text())
		for au in soup.select(".author"):
			author_1.append(au.get_text())
		for rea in soup.select(".no"):
			readNum_1.append(rea.get_text())
		for tim in soup.select(".time"):
			time_1.append(tim.get_text())
		print total[0][1].encode("utf-8"),total[1][0].encode("utf-8"),total[2][1],total[3][0]
		nu2=readNum_1



		