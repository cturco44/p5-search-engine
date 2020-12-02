import flask
from flask import request, redirect, url_for
import search

@search.app.route("/", methods=["POST", "GET"])
def show_index():
    if request.method == "GET":
        return flask.render_template("index.html")