#!/usr/bin/env python3
""" Flask app that implement a single route. """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Defines the langeages and timezone. """
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the prefered language. """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Returns the prefereed timezone. """
    return app.config['TIMEZONE']


@app.route("/", strict_slashes=False)
def index():
    """ Return a jinja template """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
