from flask import render_template, Flask, request, url_for, current_app
from apps import app

from google.appengine.ext import db
#The Model Class
class BDB(db.Model):
	photo = db.BlobProperty()
	string = db.StringProperty() 

@app.route('/')
@app.route('/index')
def index():
	return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload_db():

	#photo
	post_data = request.files['photo']
	filestream = post_data.read()

	note_data=request.form['test_get']

	upload_data = BDB()
	upload_data.photo = db.Blob(filestream)
	upload_data.string = note_data 
	upload_data.put()

	url = url_for("shows", key=upload_data.key())

	return render_template("upload.html", all_list=BDB.all())

@app.route('/show/<key>', methods=['GET'])
def shows(key):
	uploaded_data = db.get(key)
	return current_app.response_class(uploaded_data.photo)




