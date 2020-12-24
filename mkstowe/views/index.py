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


@mkstowe.app.route('/test/', methods=['GET'])
def test():
    context = {"title": "test", "desc": "test page for Michael Stowe", "load_file": "test.html"}
    return flask.render_template("master.html", **context)

