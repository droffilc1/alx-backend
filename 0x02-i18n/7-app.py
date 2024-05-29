#!/usr/bin/env python3
"""Implements Basic Babel setup."""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Mocks user login."""
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Finds users if any and sets it as global."""
    g.user = get_user()


class Config:
    """Configures available languages and time."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages."""
    # 1. Locale from url parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # 3. Locale from request headers
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """Infers appropriate time zone."""
    # Find timezone parameter in URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Find time zone from user settings
    user = get_user()
    if user and 'timezone' in users:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Starts a Flask app."""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
