"""
mkstowe firefox start page view.
URLs include:
/start/
"""
import flask
import mkstowe


@mkstowe.app.route('/start/', methods=['GET'])
def start():
    """Display /start/ route."""
    return flask.render_template("start.html")
