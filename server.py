#!/usr/bin/env python
''' Playing with templates and bootstrap. '''

from flask import Flask, render_template

my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
    return render_template('index.html')


@my_flask_app.route('/all/')
def all_news():
    return render_template('all_news.html')
if __name__ == '__main__':
    my_flask_app.run(debug=True)
