from datetime import date, datetime, timedelta
from flask import Flask, render_template, make_response
import lxml.html
import os

LIST_SIZE = 14

class SkipException (Exception):
	def __init__(self, value):
		self.value = value

def get_item(d):
	item = None
	ymd = d.strftime("%Y%m%d")
	dmy = d.strftime("%d %b %Y")
	try:
		doc = lxml.html.parse('http://ars.userfriendly.org/cartoons/?id=%s' % ymd)
	except SkipException:  
		doc = ''
	if doc:
		image = doc.xpath("/html/body/table[2]/tr/td[2]/table[1]/tr[1]/td/a/img/@src")

		if image:
			item = {
				'title': 'userfriendly : %s' % dmy,
				'link': 'http://ars.userfriendly.org/cartoons/?id=%s' % ymd,
				'image': image[0],
				'category': '',
				'date': d
			}

	return item

def userfriendly():

	start_date = date.today()-timedelta(days=LIST_SIZE-1)
	items = []

	for x in xrange(LIST_SIZE):
		d = start_date+timedelta(days=x)
		item = get_item(d)
		if item:
			items.append(item)

	response = make_response(render_template('rss.xml', items=items))
	response.headers['Content-Type'] = 'application/xml'
	response.headers['Last-Modified'] = datetime.today().strftime('%a, %d %b %Y %H:%M:%S GMT')
	response.headers['Cache-Control'] = 'public, must-revalidate, max-age=0'
	return response

def configure(app):
	app.config['PROPAGATE_EXCEPTIONS'] = True
	app.add_url_rule('/rss.xml', 'userfriendly', userfriendly)

if __name__ == '__main__':
	#app.debug = True
	configure(app)
	app.run(host='0.0.0.0')
