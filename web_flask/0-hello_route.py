#!/usr/bin/python3
""" this module starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function to print hello HBNB when following the url /"""
    return "<p>Hello HBNB!</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
