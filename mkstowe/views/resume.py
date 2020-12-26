"""
mkstowe resume view.
URLs include:
/resume/
"""
import flask
import mkstowe


@mkstowe.app.route('/resume/', methods=['GET'])
def resume():
    """Display / route."""
    context = {"title": "Resume", "desc": "Resume page for Michael Stowe", "load_file": "resume.html"}
    return flask.render_template("master.html", **context)
