#!/usr/bin/python3
"""
this module starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function to print hello HBNB when following the url /"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """function to print HBNB when following the url /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """function to print c + text when
    following the url /c/<text>"""
    text = text.replace('_', ' ')
    return "c {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
