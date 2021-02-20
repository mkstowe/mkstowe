"""
mkstowe projects view.
URLs include:
/projects/
/projects/metroid/
/projects/timber/
/projects/variegata/
/projects/cloud/
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


@mkstowe.app.route('/projects/variegata/', methods=['GET'])
def variegata():
    """Display /projects/variegata/ route."""
    context = {"title": "Project Variegata", "desc": "Project Variegata dev blog posts by Michael Stowe",
               "load_file": "variegata.html"}
    return flask.render_template("master.html", **context)


@mkstowe.app.route('/projects/variegata/<year>/<month>/<day>/', methods=['GET'])
def variegata_post(year, month, day):
    """Display post on /projects/variegata/."""
    context = {"title": "{}/{}/{}".format(year, month, day), "desc": "Project Variegata dev blog post by Michael "
               "Stowe", "load_file": "variegata_posts/{}_{}_{}.html".format(year, month, day)}
    return flask.render_template("master.html", **context)


@mkstowe.app.route('/projects/variegata/<year>/<month>/<day>/example', methods=['GET'])
def show_example(year, month, day):
    """Display post on /projects/variegata/."""
    context = {"title": "{}/{}/{}".format(year, month, day), "desc": "Project Variegata dev blog post by Michael "
               "Stowe"}
    return flask.render_template("variegata_posts/{}_{}_{}/example.html".format(year, month, day), **context)


@mkstowe.app.route('/projects/cloud/', methods=['GET'])
def cloud():
    """Display /projects/cloud/ route."""
    context = {"title": "Project Cloud", "desc": "WolverineSoft Project Cloud dev blog posts by Michael Stowe", "load_file": "cloud.html"}
    return flask.render_template("master.html", **context)


@mkstowe.app.route('/projects/cloud/<sprint>/', methods=['GET'])
def cloud_post(sprint):
    """Display post on /projects/cloud/."""
    context = {"title": sprint, "desc": "Project Cloud dev blog post by Michael Stowe",
               "load_file": "cloud_posts/{}.html".format(sprint.lower())}
    return flask.render_template("master.html", **context)
