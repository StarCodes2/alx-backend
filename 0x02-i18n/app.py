#!/usr/bin/env python3
""" Flask app that implement a single route. """
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
from typing import Dict, Optional
import pytz


class Config:
    """ Configuration for available languages and Babel settings. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict]:
    """ Returns a user dictionary based on the login_as url parameter. """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except Exception:
        return None


@app.before_request
def before_request() -> None:
    """ Sets user as a global on flask.g each request. """
    g.user = get_user()


@babel.localeselector
def get_locale() -> Optional[str]:
    """ Gets the prefered language. """
    if "locale" in request.args and \
       request.args['locale'] in app.config['LANGUAGES']:
        return request.args.get("locale")

    if g.user and g.user.get("locale") in app.config['LANGUAGES']:
        return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """ """
    tz = request.args.get("timezone", "").strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(tz).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", strict_slashes=False)
def index() -> str:
    """ Return a jinja template """
    g.current_time = format_datetime()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)