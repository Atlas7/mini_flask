from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<username>')
def hello(username=None):
    return render_template('hello.html', person_name=username)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)