from flask import Flask, render_template, make_response
import userfriendly

app = Flask(__name__, static_url_path='')

for module in [ userfriendly ]:
	module.configure(app)

if __name__ == '__main__':
	#app.debug = True
	app.run(host='0.0.0.0')
