#!/usr/bin/env python3
"""
Babel setup that get locale
from request
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """
    Gets locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render page 3-index.html
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
