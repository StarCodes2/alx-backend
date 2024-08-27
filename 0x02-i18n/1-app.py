#!/usr/bin/env python3
""" Flask app that implement a single route. """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuration for available languages and Babel settings. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """ Return a jinja template """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
