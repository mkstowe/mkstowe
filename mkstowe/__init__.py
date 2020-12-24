"""mkstowe.com package initializer."""
import flask
from datetime import datetime

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (mkstowe/config.py)
app.config.from_object('mkstowe.config')

app.config.from_envvar('MKSTOWE_SETTINGS', silent=True)


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


import mkstowe.views  # noqa: E402  pylint: disable=wrong-import-position
