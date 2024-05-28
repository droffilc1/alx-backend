#!/usr/bin/env python3
"""1-app
Implements Basic Babel setup.
Routes:
        /: displays "Hello World!"
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configures available languages and time."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Starts a Flask app."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
