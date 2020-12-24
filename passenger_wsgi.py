import os

from flask import Flask, request, render_template, redirect, url_for

project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'mkstowe/templates')
static_path = os.path.join(project_root, 'mkstowe/static')
app = Flask(__name__, template_folder=template_path, static_folder=static_path)


@app.route('/')
def index():
    """Display / route."""
    return render_template("index.html")


application = app
