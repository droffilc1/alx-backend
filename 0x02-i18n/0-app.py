#!/usr/bin/env python3
"""0-app
Basic Flask app.
Routes:
        /: displays "Hello World!"
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Starts a Flask app."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
