"""
This module is used to launch the web Application
that is designed to display all EVs' chargers placed on France
"""
import os

import flask
from flask import Flask

app = Flask(__name__, template_folder=os.path.abspath("ressources/templates/"))


@app.route("/")
def landing_page():
    """Home page for flask app"""
    print(os.getcwd(), os.listdir(os.getcwd()))
    print(os.listdir(os.path.join(os.getcwd(), "ressources")))
    return flask.render_template("home.twig")


if __name__ == "__main__":
    app.run(debug=True)
