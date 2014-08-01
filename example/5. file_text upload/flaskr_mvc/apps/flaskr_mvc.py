# -*- coding: utf-8 -*-
# all the imports

from flask import request, redirect, url_for,\
	render_template
from apps import app
from database import Database
from google.appengine.ext import db

import logging
from PIL import Image
from PIL.ExifTags import TAGS
from StringIO import StringIO

#photo class
class BDB(db.Model):
	photo = db.BlobProperty()

#database class
dataStorage = Database()

#exif function
def get_exif_data(fname):
	"""Get embedded EXIF data from image file."""
	fileinfo = {}
	try:
		img = Image.open(fname)
		if hasattr( img, '_getexif' ):
			exifinfo = img._getexif()
			print exifinfo
			if exifinfo != None:
				fileinfo = dict([(TAGS.get(key,key),value)
					for key, value in exifinfo.items()
						if type(TAGS.get(key,key)) is str])
	except IOError:
		logging.error(fname)
	return fileinfo

#get lat lon
def latlon(fil):
	lat = [float(x[0])/float(x[1]) for x in fil['GPSInfo'][2]]
	latref = fil['GPSInfo'][1]
	lon = [float(x[0])/float(x[1]) for x in fil['GPSInfo'][4]]
	lonref = fil['GPSInfo'][3]

	lat2 = lat[0] + lat[1]/60 + lat[2]/3600
	lon2 = lon[0] + lon[1]/60 + lon[2]/3600
	if latref == 'S':
		lat2 = -lat2
	if lonref == 'W':
		lon2 = -lon2
	return lat2, lon2
	
@app.route('/', methods=['GET', 'POST'])
def start():
	return render_template("index2.html")

@app.route('/map', methods=['GET', 'POST'])
def map():
	return render_template("map.html")

@app.route('/index', methods=['GET', 'POST'])
def login():
	ID = request.form['ID']
	PW = request.form['PW']
	if ID=="admin" and PW=="admin":
		return redirect(url_for('show_entries'))
	return render_template("index2.html")

@app.route('/sho', methods=['GET', 'POST'])
def show_entries():
	entries = dataStorage.out()
	return render_template('show_entries.html', entries=entries)



@app.route('/add', methods=['POST'])
def add_entry():
	storage={}
	#title save
	storage['title'] = request.form['title']

	#contents save
	storage['contents'] = request.form['contents']

	#photo key save
	post_data = request.files['photo']
	filestream = post_data.read()
	
	upload_data = BDB()
	upload_data.photo = db.Blob(filestream)
	upload_data.put()
	storage['Photo'] = upload_data.key()

	#photo exif
	exif_data = get_exif_data(StringIO(filestream))
	storage['exif']=exif_data
	latlon_r=latlon(exif_data)
	storage['latlon']=latlon_r
	dataStorage.put(storage)
	return redirect(url_for('show_entries'))


@app.route('/show/<key>', methods=['GET'])
def shows(key):
	uploaded_data = db.get(key)
	return app.response_class(uploaded_data.photo)