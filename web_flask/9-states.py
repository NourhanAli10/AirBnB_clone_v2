#!/usr/bin/python3
'''8. List of states'''

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def show_states(id=None):
    """show states"""
    states = storage.all(State)
    try:
        state = states['State.' + id] if id is not None else None
    except (KeyError):
        return render_template('9-states.html', states=None, state=None)
    return render_template('9-states.html',
                           states=states.values(), state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
