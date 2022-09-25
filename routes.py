from app import app
import users
from flask import render_template, request, redirect, session


@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password):
            return render_template("error.html", message="virheelliset kirjautumissyötteet")
        session['username'] = username
        session["role"]=users.check_admin(username)
        return redirect('/')

@app.route("/register",methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        users.register(username, password, role)
        if users.login(username,password):
            session['username'] = username
            session["role"]=users.check_admin(username)

        return redirect("/")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
