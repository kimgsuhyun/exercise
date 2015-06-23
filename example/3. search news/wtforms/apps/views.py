from flask import render_template, Flask, request
from apps import app



import urllib2
import urllib
from bs4 import BeautifulSoup

def news_s(num):
	f = urllib2.urlopen("http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1="+str(num))
	page = f.read().decode('cp949', 'ignore')
	f.close()
	soup = BeautifulSoup(page)
	result=""
	for each in soup.select(".type02_headline > li"):
		result += each.a.string +'\n'
	return result
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

	news="what"	
	U=0	
	if request.args:
		get = request.args['test_get']
		if get=="IT":
			con="IT"
			news=news_s("105")
		if get=="ECO":
			con="ECO"
			news=news_s("101")
			return render_template('index.html', news=news, contents=con)
	return render_template('index.html', news=news)



# from flask import render_template, Flask, request
# from apps import app

# from flaskext import wtf
# from flaskext.wtf import Form, TextField, TextAreaField, \
# SubmitField, validators, ValidationError

# class ContactForm(Form):
#   name = TextField("Name",  [validators.Required("Please enter your name.")])
#   email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter valid email address.")])
#   subject = TextField("Subject",  [validators.Required("Please enter a subject.")])
#   message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
#   submit = SubmitField("Send")

# @app.route('/')
# @app.route('/index', methods=['GET', 'POST'])
# def index():
# 	form = ContactForm()

# 	if request.method == 'POST':
# 		if form.validate() == False:
# 			return render_template('index.html', form=form)
# 		else:
# 			return "Nice to meet you, " + form.name.data + "!"
	
# 	return render_template('index.html', form=form)
