from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "akjshdkjashdkjhasd"

@app.route("/")
def index():
    # return "<h1>Hello World!</h1>"
    session["test"] = "Test"
    return render_template("index.html", test2="another_test")


@app.route("/success")
def success():
    return "<h1>Success!</h1>"


@app.route("/This/is/the/route")
def route():
    return "You found the route!!!"


@app.route("/process", methods=["POST"])
def process():
    valid = True
    if len(request.form["name"]) < 1:
        flash("Name is required!")
        valid=False
    if len(request.form["email"]) < 1:
        flash("Email is required!")
        valid=False
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email!")
        valid=False

    if valid == True:
        return redirect("/success")
    else:
        return redirect("/")


@app.route("/buy/<id>")
def buy(id):
    print("Someone is buying product " + id)
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
