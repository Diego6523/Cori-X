from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template(r"main.html")

@views.route("/denuncias")
def denuncias():
    return render_template(r"den.html")