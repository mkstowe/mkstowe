"""
mkstowe index (main) view.
URLs include:
/
"""
import flask
import mkstowe


@mkstowe.app.route('/', methods=['GET'])
def index():
    """Display / route."""
    return flask.render_template("index.html")
