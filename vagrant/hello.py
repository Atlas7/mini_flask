"""
A minimal Flask application
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello Page'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
