#!/usr/bin/env python3
""" Flask app that implement a single route. """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Return a jinja template """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
