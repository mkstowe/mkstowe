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
    context = {"title": "Home", "desc": "Home/About page for Michael Stowe", "load_file": "index.html"}
    return flask.render_template("master.html", **context)
