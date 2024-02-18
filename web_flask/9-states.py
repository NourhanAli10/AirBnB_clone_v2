#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all State objects."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def display_state_cities(id):
    """Display a HTML page with the list of City objects linked to the State."""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
