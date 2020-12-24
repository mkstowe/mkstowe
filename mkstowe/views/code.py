"""
mkstowe code view.
URLs include:
/code/
/code/metroid/
/code/timber/
/code/mission-o-possumble/
"""
import flask
import mkstowe


@mkstowe.app.route('/code/', methods=['GET'])
def code():
    """Display /code/ route."""
    return flask.render_template("code.html")


@mkstowe.app.route('/code/metroid/', methods=['GET'])
def metroid():
    """Display /code/metroid/ route."""
    return flask.render_template("metroid.html")


@mkstowe.app.route('/code/timber/', methods=['GET'])
def timber():
    """Display /code/timber/ route."""
    return flask.render_template("timber.html")


@mkstowe.app.route('/code/mission-o-possumble/', methods=['GET'])
def mission_o_possumble():
    """Display /code/mission-o-possumble/ route."""
    return flask.render_template("mission_o_possumble.html")
