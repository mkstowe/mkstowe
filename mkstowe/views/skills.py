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
    return flask.render_template("skills.html")
