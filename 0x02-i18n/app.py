#!/usr/bin/env python3
"""
Infer appropriate time zone
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve user information based on user ID
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Check if 'login_as' parameter is present
    in the request's query params
    """
    user_id = request.args.get('login_as')
    if user_id:
        # Get user info based on the user_id
        g.user = get_user(int(user_id))
    else:
        g.user = None


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


def get_user_locale():
    """
    Check if user is logged in and has a
    preferred locale set
    """
    if g.user and g.user.get('locale') in (
            app.config['LANGUAGES']):
        return g.user['locale']
    return None


@babel.localeselector
def get_locale():
    """
    Check if 'locale' parameter is present
    in the request and is a supported locale
    If parameter is not present or not a
    supported locale, fallback to default behavior
    """
    if 'locale' in request.args and (
            request.args['locale'] in (
                app.config['LANGUAGES'])):
        return request.args['locale']

    # Check locale from user settings
    user_locale = get_user_locale()
    if user_locale:
        return user_locale
    # Use locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user_timezone():
    """
    Check if user is logged in and has a
    preferred time zone set
    """
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass
    return None


@babel.timezoneselector
def get_timezone():
    """
    Determine the appropriate time zone for each
    request.
    """
    if 'timezone' in request.args:
        try:
            pytz.timezone(request.args['timezone'])
            return request.args['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    # Check time zone from user settings
    user_timezone = get_user_timezone()
    if user_timezone:
        return user_timezone

    # Fallback to using UTC
    return 'UTC'


@app.route('/')
def index():
    """
    Render page index.html
    """
    # Get the current time in the inferred timezone
    current_time = datetime.now(
            pytz.timezone(get_timezone()))
    # Format the current time
    formatted_time = current_time.strftime(
            '%b %d, %Y, %I:%M:%s %P')
    return render_template(
                            'index.html',
                            user=g.user,
                            current_time=formatted_time
                        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
