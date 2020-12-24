"""
mkstowe index (main) view.
URLs include:
/living_arts/
"""
import flask
import mkstowe


@mkstowe.app.route('/living_arts/', methods=['GET'])
def living_arts():
    """Display /living_arts/ route."""
    return flask.render_template("living_arts.html")
