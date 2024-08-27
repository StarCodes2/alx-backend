#!/usr/bin/env python3
""" Flask app that implement a single route. """
from flask import Flask, render_template, request
from flask_babel import _, Babel


class Config:
    """ Configuration for available languages and Babel settings. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the prefered language. """
    if "locale" in request.args and \
       request.args['locale'] in app.config['LANGUAGES']:
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """ Return a jinja template """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
