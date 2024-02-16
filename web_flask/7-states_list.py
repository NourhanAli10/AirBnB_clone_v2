#!/usr/bin/python3
"""
This module starts a Flask web application
"""

from flask import Flask , render_template
import sys
sys.path.append('../')
from models import storage
from models import *




app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', sorted_states=sorted_states)


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
