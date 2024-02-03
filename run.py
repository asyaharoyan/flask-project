"""Module providing a function printing python version."""
import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Open the index page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Open the about page"""
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])


@app.route("/contact")
def contact():
    """Open the contact page"""
    return render_template("contact.html", page_title="Contact")


@app.route("/carrieers")
def carrieers():
    """Open the contact page"""
    return render_template("carriers.html", page_title="Carriers")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)