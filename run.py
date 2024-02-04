"""Module providing a function printing python version."""
import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)


@app.route("/")
def index():
    """Open the index page"""
    return render_template("index.html")


@app.route("/about")
def about():
    """Open the about page"""
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
    """
    Open the about link
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Open the contact page"""
    if request.method == ("POST"):
        print(request.form.get("name"))
        print(request.form["email"])
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