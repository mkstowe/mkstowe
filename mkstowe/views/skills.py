"""
mkstowe skills view.
URLs include:
/skills/
"""
import flask
import mkstowe


@mkstowe.app.route('/skills/', methods=['GET'])
def skills():
    """Display /skills/ route."""
    context = {"title": "Skills", "desc": "Skills page for Michael Stowe", "load_file": "skills.html"}
    return flask.render_template("master.html", **context)
