import logging
from flask import Flask, redirect, url_for

logging.basicConfig(
    level=logging.DEBUG, format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
)


class TraefikMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        script_name = environ.get("HTTP_X_FORWARDED_PREFIX", "")
        if script_name:
            environ["SCRIPT_NAME"] = script_name

        scheme = environ.get("HTTP_X_FORWARDED_PROTO", "")
        if scheme:
            environ["wsgi.url_scheme"] = scheme

        return self.app(environ, start_response)


logging.info("Init app")
app = Flask(__name__)

logging.info("Init Traefik middleware")
app.wsgi_app = TraefikMiddleware(app.wsgi_app)


@app.route("/")
def home():
    return "HOME SWEET HOME!"


@app.route("/nothome")
def nothome():
    return redirect(url_for("home"))
