#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders index page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
