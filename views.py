from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/chat")
def home2():
    return render_template("c_interface.html")