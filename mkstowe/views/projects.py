"""
mkstowe projects view.
URLs include:
/projects/
/projects/metroid/
/projects/timber/
"""
import flask
import mkstowe


@mkstowe.app.route('/projects/', methods=['GET'])
def projects():
    """Display /projects/ route."""
    context = {"title": "Projects", "desc": "Projects page for Michael Stowe", "load_file": "projects.html"}
    return flask.render_template("master.html", **context)


@mkstowe.app.route('/projects/metroid/', methods=['GET'])
def metroid():
    """Display /projects/metroid/ route."""
    return flask.render_template("metroid.html")


@mkstowe.app.route('/projects/timber/', methods=['GET'])
def timber():
    """Display /projects/timber/ route."""
    return flask.render_template("timber.html")
