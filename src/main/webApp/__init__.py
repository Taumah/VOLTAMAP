import os

import flask
from flask import Flask
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__, template_folder=os.path.abspath('ressources/templates/'))


@app.route("/")
def landing_page():
    print(os.getcwd(), os.listdir(os.getcwd()))
    print(os.listdir(os.path.join(os.getcwd(), "ressources")))
    return flask.render_template("home.twig")


if __name__ == "__main__":
    app.run(debug=True)
