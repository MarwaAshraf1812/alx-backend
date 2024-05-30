#!/usr/bin/env python3
from flask import Flask, render_template
''' Flask App '''

app = Flask(__name__)


@app.route('/')
def index():
    ''' Index page '''
    return render_template('0-index.html',)


if __name__ == '__main__':
    app.run(debug=True)
