#!/usr/bin/env python3
"""
Basic Flask-Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configures babel objects
    Sets the avalaible languages, default
    locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Render page 1-index.html
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
