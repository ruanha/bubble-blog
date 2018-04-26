from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mr. Bubbles'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
        	'author': {'username': 'Bubble-Brian'},
        	'body': 'Bubbles... That is all'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)