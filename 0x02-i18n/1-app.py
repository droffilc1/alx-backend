#!/usr/bin/env python3
"""1-app
Implements Basic Babel setup.
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LANGUAGE'] = 'en'
app.config['BABEL_DEFAULT_DATE'] = 'UTC'
babel = Babel(app)

class Config:
    """Configures available languages."""
    LANGUAGES=['en', 'fr']
