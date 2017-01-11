from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def telltime():
	import time
	#http://stackoverflow.com/questions/3961581/in-python-how-to-display-current-time-in-readable-format
	return time.ctime() #day month date time year
	
@app.errorhandler(404)
def page_not_found(e):
	return 'Sorry, nothing is here.', 404
