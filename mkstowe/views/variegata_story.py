"""
Variegata story view.
URLs include:
/variegata/story/
"""
import flask
import mkstowe
from mkstowe.variegata.generator import generate_story


@mkstowe.app.route('/variegata/story/', methods=['GET', 'POST'])
def story():
    """Display /story/ route."""
    context = {"events": generate_story.generate_story(10)}
    return flask.render_template("variegata_story.html", **context)
