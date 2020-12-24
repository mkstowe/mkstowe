"""
mkstowe resume view.
URLs include:
/resume/
"""
import flask
import mkstowe


@mkstowe.app.route('/resume/', methods=['GET'])
def resume():
    """Display /resume/ route."""
    return flask.render_template("resume.html")
