from flask import Flask, escape, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import click


WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.route('/home')
@app.route('/')
@app.route('/index')
def index():
    user = User.query.first()
    movies =Movie.query.all()
    return render_template('index.html', user=user, movies=movies)


@app.cli.command()
def forge():
    db.create_all()
    name = 'Dang Zhang'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user =User(name=name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done!')



# @app.route('/user/<name>')
# def user_page(name):
#     return 'User page'
#
# @app.route('/user/<name>')
# def user_page(name):
#     return 'User: %s' % escape(name)
#
#
# @app.route('/test')
# def test_url_for():
#     print(url_for('hello'))
#     print(url_for('user_page', name='dangzhang'))
#     print(url_for('user_page', name='yini'))
#     print(url_for('test_url_for'))
#     print(url_for('test_url_for', num=2))
#     return 'Test page'