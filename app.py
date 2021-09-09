from flask import Flask, escape, url_for
app = Flask(__name__)


@app.route('/home')
@app.route('/')
@app.route('/index')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# @app.route('/user/<name>')
# def user_page(name):
#     return 'User page'

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='dangzhang'))
    print(url_for('user_page', name='yini'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'