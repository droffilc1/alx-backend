#!/usr/bin/env python3
"""2-app
Implements Basic Babel setup.
Routes:
        /: displays "Hello World!"
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configures available languages and time."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localselector
def get_locale():
    """Determines the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Starts a Flask app."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
