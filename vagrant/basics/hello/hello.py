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

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'post_id: %d' % post_id

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
