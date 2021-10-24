import os
import json
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/shop")
def shop():
    return render_template("shop.html", page_title="Shop")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
    return render_template("contact.html", page_title="Contact Us")


@app.route("/staff")
def staff():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("staff.html", page_title="Get to know our staff...", company=data)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)