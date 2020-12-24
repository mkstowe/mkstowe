"""
mkstowe projects view.
URLs include:
/projects/
"""
import flask
import mkstowe


@mkstowe.app.route('/projects/', methods=['GET'])
def projects():
    """Display /projects/ route."""
    context = {"title": "Projects", "desc": "Projects page for Michael Stowe", "load_file": "projects.html"}
    return flask.render_template("master.html", **context)
