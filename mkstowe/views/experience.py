"""
mkstowe experience view.
URLs include:
/experience/
"""
import flask
import mkstowe


@mkstowe.app.route('/experience/', methods=['GET'])
def experience():
    """Display /experience/ route."""
    context = {"title": "Experience", "desc": "Work, leadership, and education experience page for Michael Stowe",
               "load_file": "experience.html"}
    return flask.render_template("master.html", **context)
